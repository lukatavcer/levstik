from audioop import reverse

from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from levstik.forms.user_create_form import UserCreateForm


class RegisterView(View):

    @staticmethod
    def get(request):
        context = dict(
            form=UserCreateForm(),
        )
        return render(request, 'registration/register.html', context)

    @staticmethod
    def post(request):
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            # TODO send welcome email

            return HttpResponseRedirect(reverse('home'))

        return render(request, 'registration/register.html', dict(form=form))
