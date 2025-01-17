from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import DaySummary

class DayDetailView(DetailView):
    model = DaySummary
    template_name = 'tracker/index.html'
    context_object_name = 'day'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meals"] = self.object.meals.all()
        return context
