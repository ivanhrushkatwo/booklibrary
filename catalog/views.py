import datetime
import json

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django_ajax.decorators import ajax
from django.http import JsonResponse
from django.views import generic
from django.shortcuts import render, HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required

from .models import Book, Author
from .forms import UserCustomForm


def index(request):
    books = Book.objects.order_by("-rating")[:6]
    return render(request, 'index.html', {"books": books})


def search_category(request, pk):
    books = Book.objects.filter(category=pk)
    return render(request, "catalog/book_list.html", {"book_list": books})


def contact(request):
    return render(request, "catalog/contact.html", {})


def send_email_to_admin(request):
    # TODO add ajax response
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


@login_required
def like_book(request, pk):
    """
    Костиль
    :param request:
    :param pk:
    :return:
    """
    book = Book.objects.get(id=pk)
    book.rating += 1
    book.save()
    return render(request, "catalog/book_detail.html", {"book": book})


@login_required
def dislike_book(request, pk):
    """
    Костиль
    :param request:
    :param pk:
    :return:
    """
    book = Book.objects.get(id=pk)
    book.dislike += 1
    book.save()
    return render(request, "catalog/book_detail.html", {"book": book})


@login_required
def like_author(request, pk):
    """
    Костиль
    :param request:
    :param pk:
    :return:
    """
    author = Author.objects.get(id=pk)
    author.rating += 1
    author.save()
    return render(request, "catalog/author_detail.html", {"author": author})


def add_to_basket(request, pk):
    """
    Костиль
    :param request:
    :return:
    """

    goods = request.session.get('goods', [])
    request.session['goods'] = goods
    request.session["goods"].append(pk)
    context = {"count_goods": str(len(request.session["goods"]))}

    return JsonResponse(context)


def clear_basket(request):
    """
    Костиль
    :param request:
    :return:
    """
    request.session["goods"] = []
    return render(request, "catalog/basket.html", {})


def basket(request):
    """
    Костиль
    :param request:
    :return:
    """
    if request.session.get("goods", False):
        # books = Book.objects.filter(id__in=request.session["goods"])
        books = []
        for book_id in request.session["goods"]:
            books.append(Book.objects.get(id=book_id))
        price = sum(book.price for book in books)
    else:
        books = []
        price = 0
    return render(request, "catalog/basket.html", {"books": books, "price": price})


class About(TemplateView):
    template_name = "catalog/about.html"


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 8


class AuthorDetailView(generic.DetailView):
    model = Author

    def get_context_data(self, **kwargs):
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        context["books"] = Book.objects.filter(author=self.kwargs["pk"])
        return context
