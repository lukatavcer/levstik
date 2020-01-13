from django.views.generic.base import View
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from levstik.models import Winner


class WinnerProfileView(View):

    @staticmethod
    def get(request, slug):
        try:
            winner_id = int(slug.split('-')[0])
        except ValueError:
            raise Http404()

        winner = get_object_or_404(Winner, id=winner_id)
        context = dict(
            winner=winner
        )

        template = "winner_profile/winner_profile.html"
        return render(request, template, context)
