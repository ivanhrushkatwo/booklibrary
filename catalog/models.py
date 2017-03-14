from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class CustomUser(AbstractUser):

    image = models.ImageField(blank=True)

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.id)])

    def __str__(self):
        return "{}".format(self.username)


class Language(models.Model):
    name = models.CharField(
        max_length=64
    )

    def __str__(self):
        return self.name


class CategoryBook(models.Model):

    name = models.CharField(
        verbose_name="Categories of books",
        max_length=64
    )

    description = models.TextField(
        verbose_name="Description",
        null=True,
        blank=True
    )

    def __str__(self):
        return "{}".format(self.name)


class GenreBook(models.Model):

    name = models.CharField(
        max_length=32,
        unique=True
    )

    description = models.TextField(
        verbose_name="Description",
        null=True,
        blank=True
    )

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = "Genre of book"
        verbose_name_plural = "Genres of books"


class Book(models.Model):

    title = models.CharField(
        max_length=200
    )

    author = models.ForeignKey(
        'Author',
        on_delete=models.SET_NULL,
        null=True
    )

    category = models.ForeignKey(
        CategoryBook,
        models.PROTECT,
    )

    summary = models.TextField(
        max_length=1000,
        help_text="Enter a brief description of the book"
    )

    in_stock = models.BooleanField(
        default=False,
        verbose_name="In stock"
    )

    price = models.IntegerField(
        default=0,
        verbose_name="Price"
    )

    rating = models.IntegerField(
        default=0,
        verbose_name="Rating"
    )

    dislike = models.IntegerField(
        default=0,
        verbose_name="Dislike",

    )

    isbn = models.CharField(
        'ISBN',
        max_length=13,
        help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>'
    )

    genre = models.ManyToManyField(
        GenreBook,
        blank=True,
        help_text="Select a genre for this book",
    )

    language = models.ForeignKey(
        Language,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    image = models.ImageField(
        upload_to="img_book",
        verbose_name="Image",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"


class Author(models.Model):

    first_name = models.CharField(
        max_length=100
    )

    last_name = models.CharField(
        max_length=100
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    date_of_death = models.DateField(
        'Died',
        null=True,
        blank=True
    )

    biography = models.TextField(
        verbose_name="Biography",
        null=True,
        blank=True
    )

    image = models.ImageField(
        upload_to="img_author",
        verbose_name="Author image",
        null=True,
        blank=True
    )

    rating = models.IntegerField(
        default=0,
        verbose_name="Rating"
    )

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return '{} {}'.format(self.last_name, self.first_name)
