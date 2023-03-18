from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView

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
    prompt = f'''Give me a recipe with the following ingredients: {user_prompt}. But, give the recipe by filling out the following html form as template:" \
    <div>
        <h2 id="recipe_name"></h2>
        <p id="recipe_description"></p>
        <h2 id="ingredients"></h2>
        <ul id="ingredient_list">
            <li id="ingredient_1"></li>
            <li id="ingredient_2"></li>
        </ul>
        <h2 id="instructions"></h2>
        <ol id="instruction_list">
            <li id="step_1"></li>
            <li id="step_2"></li>
        </ol>
        <p id="prep_time"></p>
        <p id="cooking_time"></p>
        <p id="servings"></p>
        <p id="total_calories"></p>
        <p id="calories_per_serving"></p>
        <p id="num_protein"></p>
        <p id="num_cabs"></p>
        <p id="num_fat"></p>
    </div>'''

    openai.api_key = open("main_app/key.txt", "r").read().strip('\n')
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user", "content": prompt
        }]
    )

    chatgpt_recipe = completion["choices"][0]["message"]["content"]
    return render(request, 'recipes/show_recipe.html', {"recipe": chatgpt_recipe})