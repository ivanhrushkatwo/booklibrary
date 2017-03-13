import datetime
import json

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

    # print(request.session.items())
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    num_books = Book.objects.all().count()
    num_authors = Author.objects.count()

    return render(
        request,
        'index.html',
        context={
            'num_books': num_books,
            'num_authors': num_authors,
            'num_visits': num_visits,
        }
    )


def search_category(request, pk):

    books = Book.objects.filter(category=pk)

    return render(
        request,
        "catalog/book_list.html",
        {
            "book_list": books
        }
    )


@login_required
def like_book(request, pk):

    book = Book.objects.get(id=pk)
    book.rating += 1
    book.save()

    return render(request, "catalog/book_detail.html", {"book": book})


@login_required
def dislike_book(request, pk):

    book = Book.objects.get(id=pk)
    book.dislike += 1
    book.save()

    return render(request, "catalog/book_detail.html", {"book": book})


@login_required
def like_author(request, pk):

    author = Author.objects.get(id=pk)
    author.rating += 1
    author.save()

    return render(request, "catalog/author_detail.html", {"author": author})


def add_to_basket(request, pk):
    goods = request.session.get('goods', [])

    request.session['goods'] = goods
    request.session["goods"].append(pk)
    return HttpResponse(json.dumps(request.session["goods"]), content_type="application/json")


def clear_basket(request):
    request.session["goods"] = []
    return render(request, "catalog/basket.html", {})


def basket(request):
    books = Book.objects.filter(id__in=request.session["goods"])
    price = sum(book.price for book in books)
    return render(request, "catalog/basket.html", {"books": books, "price": price})


class About(TemplateView):
    template_name = "catalog/about.html"


# class RegistrationView(FormView):
#     template_name = "registration/registration_form.html"
#     form_class = UserCustomForm
#     success_url = "/"
#
#     def form_valid(self, form):
#         form.save()
#         return super(RegistrationView, self).form_valid(form)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 8


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 7


class AuthorDetailView(generic.DetailView):
    model = Author

    def get_context_data(self, **kwargs):
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        context["books"] = Book.objects.filter(author=self.kwargs["pk"])

        return context
