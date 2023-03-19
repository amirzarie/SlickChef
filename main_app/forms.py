from django.forms import ModelForm
from .models import Recipe

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['recipe_name', 'ingredients', 'instructions', 'servings', 'total_calories', 'calories_per_serving', 'total_protein', 'total_carbs', 'total_fat']