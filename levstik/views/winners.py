from django.views.generic.base import View
from django.shortcuts import render

from levstik.models.winner import Winner


class WinnersView(View):

    @staticmethod
    def get(request):
        context = dict(
            winners=Winner.objects.all()
        )
        return render(request, "levstik/winners.html", context)
