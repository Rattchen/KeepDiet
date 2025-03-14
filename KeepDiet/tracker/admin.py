from django.contrib import admin
from .models import Meal, DaySummary, TrackerProfile, Measurements, Activity, WeightRecord

admin.site.register(Meal)
admin.site.register(DaySummary)
admin.site.register(TrackerProfile)
admin.site.register(Measurements)
admin.site.register(Activity)
admin.site.register(WeightRecord)