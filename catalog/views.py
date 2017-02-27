import datetime

from django.views import generic
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import permission_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from .models import Book, Author, GenreBook, CustomUser
from .forms import UserCustomForm


def index(request):

    # print(request.session.items())
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()

    num_authors = Author.objects.count()  # The 'all()' is implied by default.

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


class About(TemplateView):
    template_name = "catalog/about.html"


class RegistrationView(FormView):
    template_name = "registration/registration_form.html"
    form_class = UserCustomForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super(RegistrationView, self).form_valid(form)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 3


class BookDetailView(generic.DetailView):

    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 3


class AuthorDetailView(generic.DetailView):
    model = Author

    def get_context_data(self, **kwargs):
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        context["books"] = Book.objects.filter(author=self.kwargs["pk"])

        return context


class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'
    initial = {'date_of_death': str(datetime.datetime.now().date())}


class AuthorUpdate(UpdateView):
    model = Author
    fields = "__all__"


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')


class BookCreate(CreateView):
    model = Book
    fields = "__all__"


class BookUpdate(UpdateView):
    model = Book
    fields = "__all__"


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy("books")
