from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('main_app/get_ingredients/', views.get_ingredients, name='get_ingredients'),
    path('recipes/show_recipe/', views.show_recipe, name='show_recipe'),
    path('recipes/user_index/', views.recipes_index, name='user_index'),

    # Accounts
    path('accounts/signup/', views.signup, name='signup'),
]