from django import forms

from django.forms import ModelForm
from .models import Book, CustomUser, Author
from django.core.exceptions import ValidationError

from django.utils.translation import ugettext_lazy as _
import datetime  # for checking renewal date range.


class BookModelForm(ModelForm):
    author = forms.ChoiceField(choices=Author.objects.all(), widget=forms.Select())

    class Meta:
        model = Book
        fields = ["title", "author", "summary", "isbn", "genre", "language"]


class UserCustomForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput(), min_length=8)
    # email    = forms.EmailField(required=True)

    def save(self, commit=True):

        user = super(UserCustomForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'image',)
