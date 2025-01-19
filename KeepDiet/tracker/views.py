import os
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import DetailView, TemplateView, View
from fatsecret import Fatsecret
from .models import DaySummary

FS_CONSUMER = str(os.getenv('FS_CONSUMER'))
FS_SECRET = str(os.getenv('FS_SECRET'))


class DayDetailView(DetailView):
    model = DaySummary
    template_name = 'tracker/index.html'
    context_object_name = 'day'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meals"] = self.object.meals.all()
        return context

class SearchPageView(TemplateView):
    template_name = "tracker/search_results.html"

class SearchView(View):
    def get(self, request):
        query = request.GET.get('search', '')
        fs = Fatsecret(FS_CONSUMER, FS_SECRET)
        res = fs.foods_search(query)
        return JsonResponse({"results":res})
