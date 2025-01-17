from django.shortcuts import render
from django.http import HttpResponse
from .models import DaySummary

def index(request):
    day = DaySummary.objects.get(id=1)
    meals = day.meals.all()
    return render(request, 'tracker/index.html', context={'day':day, 'meals':meals})