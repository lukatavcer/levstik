from django.contrib.auth.forms import PasswordChangeForm


class ChangePasswordForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].label = 'Staro geslo'
        self.fields['new_password1'].label = 'Novo geslo'
        self.fields['new_password2'].label = 'Potrdi novo geslo'

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
