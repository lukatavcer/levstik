from django.views.generic.base import View
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from enroll.models import User


class ProviderPublicProfileView(View):

    @staticmethod
    def get(request, slug):
        try:
            provider_id = int(slug.split('-')[0])
        except ValueError:
            raise Http404()

        provider = get_object_or_404(User, id=provider_id)
        context = dict(
            provider=provider,
            profile=provider.provider_public_profile,
        )

        template = "public_profile/public_profile.html"
        return render(request, template, context)
