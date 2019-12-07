from django.views.generic.base import View
from django.shortcuts import render


class DashboardView(View):

    @staticmethod
    def get(request):
        user = request.user
        context = dict()

        if request.user.is_provider:
            context["active_jobs"] = request.user.provider_jobs.filter(finished__isnull=True)
            context["finished_jobs"] = request.user.provider_jobs.filter(finished__isnull=False)
            template = "dashboard/provider_dashboard.html"
        else:
            context["active_jobs"] = request.user.customer_jobs.filter(finished__isnull=True)
            context["finished_jobs"] = request.user.customer_jobs.filter(finished__isnull=False)
            template = 'dashboard/customer_dashboard.html'

        return render(request, template, context)
