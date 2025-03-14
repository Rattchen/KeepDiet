from django.contrib import admin
from .models import Meal, DaySummary, TrackerProfile, Measurements

admin.site.register(Meal)
admin.site.register(DaySummary)
admin.site.register(TrackerProfile)
admin.site.register(Measurements)