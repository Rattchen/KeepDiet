from django.contrib import admin
from .models import Meal, DaySummary, TrackerProfile

admin.site.register(Meal)
admin.site.register(DaySummary)
admin.site.register(TrackerProfile)