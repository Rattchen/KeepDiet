from django.db import models
from django.conf import settings

class TrackerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s profile"

class Measurements(models.Model):
    """ Holds body measurements to keep track of the progress"""
    
    unit = models.CharField(max_length=25, null=True, blank=True)
    arm = models.FloatField(null=True, blank=True)
    chest = models.FloatField(null=True, blank=True)
    waist = models.FloatField(null=True, blank=True)
    stomach = models.FloatField(null=True, blank=True)
    hips = models.FloatField(null=True, blank=True)
    thighs = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Measurements for {self.day}"

class DaySummary(models.Model):
    """ Holds additional info about the whole day, like activity or weight"""
    #TODO: Weight should update user's profile if provided

    user = models.ForeignKey(TrackerProfile, on_delete=models.CASCADE)
    weight = models.FloatField(null=True, blank=True)
    measurements = models.ForeignKey(Measurements, on_delete=models.CASCADE, related_name="day", null=True, blank=True)
    was_active = models.BooleanField()
    activity_name = models.CharField(max_length=250, null=True, blank=True)
    activity_quantity = models.FloatField(null=True, blank=True)
    activity_unit = models.CharField(max_length=25, null=True, blank=True)

    @property
    def total_calories(self):
        return sum(meal.calories or 0 for meal in self.meals.all())

    def __str__(self):
        return f"Day summary for {self.user.user.username}"

class Meal(models.Model):
    """ Holds info pertaining to a single meal"""

    class MealType(models.TextChoices):
        BREAKFAST = 'breakfast', 'Breakfast'
        LUNCH = 'lunch', 'Lunch'
        DINNER = 'dinner', 'Dinner'
        DESSERT = 'dessert', 'Dessert'
        SUPPER = 'supper', 'Supper'
        SNACK = 'snack', 'Snack'
        DRINK = 'drink', 'Drink'
        OTHER = 'other', 'Other'

    date = models.DateField()
    time = models.TimeField()
    category = models.CharField(max_length=25, choices=MealType.choices)
    name = models.CharField(max_length=250)
    quantity = models.FloatField(null=True, blank=True)
    unit = models.CharField(max_length=25, null=True, blank=True)
    calories = models.IntegerField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    day = models.ForeignKey(DaySummary, on_delete=models.CASCADE, related_name='meals')

