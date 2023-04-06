from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import json
import os

# Auth
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Need to add LoginRequiredMixin and login_required to all views we want to restrict. Leaving it out for now for ease of testing. - Ryan

# Model
from main_app.models import Recipe

# API
import openai


# Create your views here.



def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def signup(request):
    error_message = ''
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def get_ingredients(request):
    return render(request, 'main_app/get_ingredients.html')


def show_recipe(request):
    user_prompt = request.POST

    prompt = f'''
    Give me a recipe using the following ingredients: {user_prompt}. But, return your answer by filling out the following python dictionary object (don't add additional information fields). Also, if the recipe isn't a well-known dish (e.g., lasagna), give it a quirky/funny name:
    {{
        "recipe_name": "",
        "ingredients": [],
        "instructions": [],
        "servings": ,
        "total_calories": ,
        "calories_per_serving": ,
        "total_protein": ,
        "total_carbs": ,
        "total_fat": 
    }}'''

    # openai.api_key = open("main_app/key.txt", "r").read().strip('\n')
    openai.api_key = os.getenv('ChatGPT-API-Key')
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user", "content": prompt
        }]
    )

    chatgpt_recipe = completion["choices"][0]["message"]["content"]
    print(chatgpt_recipe)
    chatgpt_recipe_dict = json.loads(chatgpt_recipe)
    print(chatgpt_recipe_dict)
    return render(request, 'recipes/show_recipe.html', {"recipe": chatgpt_recipe_dict, "user_prompt": user_prompt})

class RecipeCreate(CreateView):
    model = Recipe
    fields = ['recipe_name', 'ingredients', 'instructions', 'servings', 'total_calories', 'calories_per_serving', 'total_protein', 'total_carbs', 'total_fat']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_prompt'] = self.request.POST.get('user_prompt')
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def recipes_index(request):
    recipes = Recipe.objects.filter(user=request.user)
    return render(request, 'recipes/user_index.html', {'recipes': recipes})

def recipes_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    recipe = {
        "recipe_name": recipe.recipe_name,
        "ingredients": recipe.ingredients.split(", "),
        "instructions": recipe.instructions.split("., "),
        "servings": recipe.servings,
        "total_calories": recipe.total_calories,
        "calories_per_serving": recipe.calories_per_serving,
        "total_protein": recipe.total_protein,
        "total_carbs": recipe.total_carbs,
        "total_fat": recipe.total_fat,
        "id": recipe.id
    }
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

class RecipeUpdate(UpdateView):
    model = Recipe
    fields = ['ingredients', 'instructions', 'servings', 'total_calories', 'calories_per_serving', 'total_protein', 'total_carbs', 'total_fat']

class RecipeDelete(DeleteView):
    model = Recipe
    success_url = '/recipes/'    