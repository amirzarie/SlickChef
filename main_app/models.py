from django.db import models
from django.urls import reverse


# Create your models here.
 
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredient = models.CharField(max_length=250)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'recipe_id: self.id'})
