from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Recipe(models.Model):
    ingredients = models.TextField(max_length=500)
    recipe = models.TextField(max_length=2500)

    def __str__(self):
        return f"Recipe: {self.recipe}"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'recipe_id': self.id})