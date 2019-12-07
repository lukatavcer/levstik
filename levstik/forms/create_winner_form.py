from django.forms import *
from levstik.models import Winner


class CreateWinnerForm(ModelForm):

    class Meta:
        model = Winner
        # date = DateTimeField(input_formats=["%d/%m/%Y %H:%M"])
        fields = ['first_name', 'last_name', 'birth_date', 'description']
        labels = dict(
            first_name="Ime",
            last_name="Priimek",
            birth_date="Datum rojstva",
            description="Opis"
        )

    # def __init__(self, *args, **kwargs):
    #     # self.customer = kwargs.pop('customer', None)
    #     # self.post = kwargs.pop('post', None)
    #     super(CreateWinnerForm, self).__init__(*args, **kwargs)
    #
    #     self.fields['area'].widget = HiddenInput()
    #
    #     for visible in self.visible_fields():
    #         visible.field.widget.attrs['class'] = 'form-control'
    #
    #     if self.customer:
    #         self.initial.update(
    #             dict(
    #                 name=self.customer.get_full_name(),
    #                 address=self.customer.address,
    #                 city=self.customer.city,
    #                 post=self.customer.post,
    #             )
    #         )
    #
    #     if self.post:
    #         self.initial['post'] = self.post
    #
    # def save(self, commit=True):
    #     instance = super(CreateJobForm, self).save(commit=False)
    #     instance.customer = self.customer
    #
    #     area = self.cleaned_data['area']
    #     discount = 1
    #     if area >= 90:
    #         discount = 0.95
    #     instance.price = area * 0.21 * discount
    #
    #     if commit:
    #         instance.save()
    #     return instance
