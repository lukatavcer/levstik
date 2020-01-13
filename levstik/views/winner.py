from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import View

from levstik.forms.create_winner_form import CreateWinnerForm


class CreateWinnerView(LoginRequiredMixin, View):
    @staticmethod
    def get(request):
        context = dict(
            form=CreateWinnerForm()
        )

        return render(request, "levstik/winner_create.html", context)

    @staticmethod
    def post(request):
        user = request.user
        form = CreateWinnerForm(request.POST, request.FILES, created_by=user)

        if form.is_valid():
            form.save()

            messages.success(request, "Dobitnik je bil ustvarjen!")
            return HttpResponseRedirect(reverse('home'))

        context = dict(
            form=form
        )

        return render(request, "levstik/winner_create.html", context)
