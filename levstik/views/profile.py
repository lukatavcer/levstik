from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse
from django.utils.timezone import now
from django.views.generic.base import View
from django.shortcuts import render, redirect

from levstik.forms.change_password_form import ChangePasswordForm
from levstik.forms.personal_info_form import PersonalInfoForm


class ProfileView(LoginRequiredMixin, View):

    @staticmethod
    def get(request):
        user = request.user
        context = dict(
            personal_info_form=PersonalInfoForm(instance=user),
            change_password_form=ChangePasswordForm(user),
        )
        context['personal_info_tab'] = 'active'
        template = "profile/customer.html"

        return render(request, template, context)

    @staticmethod
    def post(request):
        user = request.user
        context = dict()
        change_password_form = None
        personal_info_form = None

        template = "profile/customer.html"

        if 'change_password' in request.POST:
            change_password_form = ChangePasswordForm(user=user, data=request.POST)
            if change_password_form.is_valid():
                change_password_form.save()
                messages.success(request, 'Uspešno ste zamenjali svoje geslo.')
                return redirect(reverse('profile'))
            context['security_tab'] = 'active'
        elif 'public_profile' in request.POST:
            # provider_public_profile_form = ProviderPublicProfileForm(request.POST, instance=user.provider_public_profile)
            # if provider_public_profile_form.is_valid():
            #     provider_public_profile_form.save()
            #     messages.success(request, 'Public profile updated.')
            #     return redirect(reverse('profile'))
            context['public_profile_tab'] = 'active'
        else:
            personal_info_form = PersonalInfoForm(request.POST, instance=user)
            if personal_info_form.is_valid():
                personal_info_form.save()
                messages.success(request, 'Osebni podatki so bili posodobljeni.')
                return redirect(reverse('profile'))
            context['personal_info_tab'] = 'active'

        context['personal_info_form'] = personal_info_form if personal_info_form else PersonalInfoForm(instance=user)
        context['change_password_form'] = change_password_form if change_password_form else ChangePasswordForm(user)

        return render(request, template, context)
