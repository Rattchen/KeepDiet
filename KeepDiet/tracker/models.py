from django.db import models

class DaySummary(models.Model):
    """ Holds additional info about the whole day, like activity or weight"""
    #TODO: Weight should update user's profile if provided

    weight = models.FloatField(null=True, blank=True)
    was_active = models.BooleanField()
    activity_name = models.CharField(max_length=250, null=True, blank=True)
    activity_quantity = models.FloatField(null=True, blank=True)
    activity_unit = models.CharField(max_length=25, null=True, blank=True)

    @property
    def total_calories(self):
        return sum(meal.calories or 0 for meal in self.meals.all())


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

