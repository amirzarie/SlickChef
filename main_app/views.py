from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Recipe
import openai


def get_recipe(request):
    prompt = "user input"

    openai.api_key = open("key.txt", "r").read().strip('\n')
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = [{
            "role": "user", "content": prompt
        }]
    )

    ChatGPT_recipe = completion["choices"][0]["message"]["content"]

from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Recipe

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def recipes_index(request, recipe_id):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/index.html', { 'recipes': recipes})

def recipes_detail(request,recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipes/detail.html', {'recipe': recipe})

class RecipeCreate(CreateView):
    model = Recipe
    fields = ['name','ingredient']

    
class RecipeDelete(DeleteView):
    model = Recipe
    success_url = '/recipes/'
