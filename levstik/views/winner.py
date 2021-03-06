from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic.base import View

from levstik.forms.create_winner_form import CreateWinnerForm
from levstik.models import Winner


class CreateWinnerView(LoginRequiredMixin, View):
    @staticmethod
    def get(request):
        context = dict(
            form=CreateWinnerForm()
        )

        return render(request, "winners/winner_create.html", context)

    @staticmethod
    def post(request):
        user = request.user
        form = CreateWinnerForm(request.POST, request.FILES, created_by=user)

        if form.is_valid():
            form.save()

            messages.success(request, "Nagrajenec je bil ustvarjen!")
            return HttpResponseRedirect(reverse('home'))

        context = dict(
            form=form
        )

        return render(request, "winners/winner_create.html", context)


class EditWinnerView(LoginRequiredMixin, View):
    @staticmethod
    def get(request, id):
        winner = get_object_or_404(Winner, id=id)
        context = dict(
            form=CreateWinnerForm(instance=winner)
        )

        return render(request, "winners/winner_edit.html", context)

    @staticmethod
    def post(request, id):
        user = request.user
        winner = get_object_or_404(Winner, id=id)
        form = CreateWinnerForm(instance=winner, data=request.POST, files=request.FILES, created_by=user)

        if form.is_valid():
            form.save()
            messages.success(request, "Nagrajenec je bil posodobljen!")
            return HttpResponseRedirect(reverse('winner_profile', args=[id]))

        context = dict(
            form=form
        )

        return render(request, "winners/winner_create.html", context)
