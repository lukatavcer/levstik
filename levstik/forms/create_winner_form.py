from django.forms import *
from levstik.models import Winner


class CreateWinnerForm(ModelForm):

    class Meta:
        model = Winner
        fields = ['first_name', 'last_name', 'birth_date', 'awarded_date', 'description', 'image']
        labels = dict(
            first_name="Ime",
            last_name="Priimek",
            birth_date="Datum rojstva",
            awarded_date="Datum prejema nagrade",
            description="Opis",
            image="Slika"
        )

    def __init__(self, *args, **kwargs):
        self.created_by = kwargs.pop('created_by', None)
        super(CreateWinnerForm, self).__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

        if self.initial.get('awarded_date'):
            self.initial['awarded_date'] = self.initial['awarded_date'].strftime("%-d. %-m. %Y")
        if self.initial.get('birth_date'):
            self.initial['birth_date'] = self.initial['birth_date'].strftime("%-d. %-m. %Y")

    def save(self, commit=True):
        instance = super(CreateWinnerForm, self).save(commit=False)
        instance.created_by = self.created_by

        if commit:
            instance.save()
        return instance
