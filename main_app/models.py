from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=2500)
    instructions = models.CharField(max_length=2500)
    servings = models.IntegerField()
    total_calories = models.IntegerField()
    calories_per_serving = models.IntegerField()
    total_protein = models.IntegerField()
    total_carbs = models.IntegerField()
    total_fat = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Recipe: {self.recipe_name}"

    def get_absolute_url(self):
        return reverse('user_index')