from django.forms import *
from django.contrib.auth.models import User


class PersonalInfoForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']
        labels = dict(
            username='E-pošta',
            first_name='Ime',
            last_name='Priimek'
        )
        widgets = dict(
            username=EmailInput,
        )

    def __init__(self, *args, **kwargs):
        super(PersonalInfoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
