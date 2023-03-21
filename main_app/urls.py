from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('recipes/get_ingredients/', views.get_ingredients, name='get_ingredients'),
    path('recipes/show_recipe/', views.show_recipe, name='show_recipe'),
    path('recipes/', views.recipes_index, name='user_index'),
    path('recipes/create_recipe/', views.RecipeCreate.as_view(), name='recipes_create'),
    path('recipes/<int:recipe_id>/', views.recipes_detail, name='recipe_detail'),
    path('recipes/<int:pk>/update/', views.RecipeUpdate.as_view(), name='recipes_update'),
    path('recipes/<int:pk>/delete/', views.RecipeDelete.as_view(), name='recipes_delete'),

    # Accounts
    path('accounts/signup/', views.signup, name='signup'),
]