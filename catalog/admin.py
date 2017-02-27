from django.contrib import admin
from .models import Author, GenreBook, Language, CustomUser, User, Book, CategoryBook


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


admin.site.register(Language)
admin.site.register(Author)
admin.site.register(GenreBook)
admin.site.register(CustomUser)
admin.site.register(User)
admin.site.register(Book)
admin.site.register(CategoryBook)
