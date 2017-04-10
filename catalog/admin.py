from django.contrib import admin
from .models import Author, GenreBook, Language, CustomUser, User, Book, CategoryBook, Publisher


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "price", "isbn")

admin.site.register(Language)
admin.site.register(Author)
admin.site.register(GenreBook)
admin.site.register(CustomUser)
admin.site.register(User)
admin.site.register(CategoryBook)
admin.site.register(Publisher)
