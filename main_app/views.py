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