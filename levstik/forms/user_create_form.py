from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        labels = dict(
            username='E-pošta'
        )
        widgets = dict(
            username=forms.EmailInput,
        )

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = 'Geslo'
        self.fields['password2'].label = 'Potrdi geslo'

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
