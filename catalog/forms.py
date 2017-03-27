from django import forms

from .models import CustomUser


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
