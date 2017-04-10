from django import forms
from simple_search import search_form_factory

from .models import CustomUser, Book


SearchForm = search_form_factory(Book.objects.all(),
                                 ['^title', 'description', 'author'])


class UserCustomForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), min_length=8)

    def save(self, commit=True):
        user = super(UserCustomForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'image',)
