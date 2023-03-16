from django.db import models
from django.urls import reverse


class Recipe(models.Model):
    ingredients = models.TextField(max_length=500)
    recipe = models.TextField(max_length=2500)

    def __str__(self):
        return f"Recipe: {self.recipe}"


# class Ingredients(models.Model):
#     ingredients = models.TextField(max_length=500)
#     recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"Ingredients: {self.ingredients}"
#
#     def get_absolute_url(self):
#         return reverse('detail', kwargs={'recipe_id': self.id})