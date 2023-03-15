from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from .forms import RecipeForm

# Auth
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Need to add LoginRequiredMixin and login_required to all views we want to restrict. Leaving it out for now for ease of testing. - Ryan

# Model
from .models import Recipe

# API
import openai


def get_recipe(user_prompt):
    prompt = f"Give me a recipe using the following ingredients: {user_prompt}"

    openai.api_key = open("key.txt", "r").read().strip('\n')
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = [{
            "role": "user", "content": prompt
        }]
    )

    ChatGPT_recipe = completion["choices"][0]["message"]["content"]

    return ChatGPT_recipe


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


def recipes_index(request, recipe_id):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/index.html', { 'recipes': recipes})


def recipes_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipes/detail.html', {'recipe': recipe})


class RecipeCreate(CreateView):
    model = Recipe
    fields = ["recipe"]


class RecipeDelete(DeleteView):
    model = Recipe
    success_url = '/recipes/'


def create_recipe(request):
    user_prompt = request.POST
    prompt = f"Give me a recipe using the following ingredients: {user_prompt}"

    openai.api_key = open("key.txt", "r").read().strip('\n')
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user", "content": prompt
        }]
    )

    chatgpt_recipe = completion["choices"][0]["message"]["content"]

    form = RecipeForm(initial={"recipe": chatgpt_recipe})
    if form.is_valid():
        new_recipe = form.save(commit=False)
        new_recipe.save()
        return redirect('detail', recipe_id=new_recipe.id)
    return render(request, 'create_recipe.html', {'form': form})
