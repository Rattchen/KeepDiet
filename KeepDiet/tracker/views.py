import os
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
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

def apicalltest(request):
    fs = Fatsecret(FS_CONSUMER, FS_SECRET)
    try:
        banana = fs.foods_search("banana")
        bananaid = banana[0]['food_id']
        info = fs.food_get_v2(bananaid)
        print(info)
    except:
        print("Nothing found!")
    return HttpResponse('Test')
