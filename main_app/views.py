from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView

# Auth
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Model
from .models import Recipe

# API
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
