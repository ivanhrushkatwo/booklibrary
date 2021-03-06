import os

from wsgiref.util import FileWrapper
from django.core.mail import send_mail, BadHeaderError
from django.http import StreamingHttpResponse
from django.http import JsonResponse
from django.views import generic
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from django.contrib.postgres.search import SearchVector

from .models import Book, Author


def index(request):
    books = Book.objects.all()[:6]
    return render(request, 'index.html', {"books": books})


def search_category(request, pk):
    books = Book.objects.filter(category=pk)
    return render(request, "catalog/book_list.html", {"book_list": books})


def search(request):
    q = request.GET.get("q", "")
    books = Book.objects.annotate(
        search=SearchVector("title", "summary", "author__first_name", "author__last_name", "category__name"),
    ).filter(search=q)
    return render(request, "catalog/book_list.html", {"book_list": books})


def contact(request):
    return render(request, "catalog/contact.html", {})


def send_email_to_admin(request):
    from_email = request.POST.get("email")
    subject = request.POST.get("subject")
    massage = request.POST.get("massage")
    if subject and massage and from_email:
        try:
            send_mail(subject, massage, from_email, ['ivanhrushka.py@gmail.com'])
        except BadHeaderError:
            return JsonResponse({"data": "Invalid header found."})

        return JsonResponse({"data": "Message sent successfully"})
    else:
        return JsonResponse({"data": "false"})


def add_to_basket(request, pk):
    goods = request.session.get("goods", {})
    request.session["goods"] = goods
    if pk not in request.session["goods"]:
        request.session["goods"][pk] = 1
    else:
        request.session["goods"][pk] += 1
    context = {"count_goods": str(sum(list(request.session["goods"].values())))}
    return JsonResponse(context)


def delete_one_book_from_basket(request, pk):
    request.session.modified = True
    request.session["goods"][pk] -= 1
    if request.session["goods"][pk] == 0:
        del request.session["goods"][pk]
        context = {"count_goods": str(sum(list(request.session["goods"].values()))), "empty": "true"}
        return JsonResponse(context)
    context = {"count_goods": str(sum(list(request.session["goods"].values())))}
    return JsonResponse(context)


def clear_basket(request):
    request.session["goods"] = {}
    return render(request, "catalog/basket.html", {})


def delete_from_basket(request):
    if request.method == "POST":
        pk = request.POST["pk"]
        if pk in request.session["goods"]:
            request.session.modified = True
            del request.session["goods"][pk]
            return JsonResponse(
                {
                    "count_goods": str(sum(list(request.session["goods"].values()))),
                 }
            )
    return redirect('basket')


def basket(request):
    if request.session.get("goods", False):
        books = []
        for book_id in request.session["goods"].keys():
            book = Book.objects.get(id=book_id)
            book.c = request.session["goods"][book_id]
            book.amount = book.c * book.price
            books.append(book)
        price = sum(book.price * book.c for book in books)
        num_of_book = sum(book.c for book in books)
    else:
        books = []
        price = 0
        num_of_book = 0
    return render(request, "catalog/basket.html", {"books": books, "price": price, "num_of_book": num_of_book})


def download_sample(request, pk):
    pth = Book.objects.get(id=pk)
    file = pth.free_sampler_pdf_file.path
    resp = StreamingHttpResponse(FileWrapper(open(file, 'rb'), 8192), content_type="application/pdf")
    resp['Content-Length'] = os.path.getsize(file)
    resp["Content-Disposition"] = "attachment; filename=" + file
    return resp


class About(TemplateView):
    template_name = "catalog/about.html"


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Book


class AuthorDetailView(generic.DetailView):
    model = Author

    def get_context_data(self, **kwargs):
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        context["books"] = Book.objects.filter(author=self.kwargs["pk"])
        return context
