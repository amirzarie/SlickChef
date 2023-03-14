from django.db import models
from django.urls import reverse


class Recipe(models.Model):
    recipe = models.TextField(max_length=2500)

    def __str__(self):
        return f"Recipe: {self.recipe}"