from django.shortcuts import render
from django.views.generic.base import View, TemplateView

from levstik.models import Winner


class HomeView(View):
    @staticmethod
    def get(request):
        user = request.user
        context = dict(
            winners=Winner.objects.all()
        )

        return render(request, "levstik/home.html", context)


class AboutUs(TemplateView):
    @staticmethod
    def get(request):
        return render(request, "levstik/about_us.html")
