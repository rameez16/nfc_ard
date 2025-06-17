from django.db import models

# Create your models here.

from django.db import models

class BusinessCard(models.Model):
    username = models.SlugField(max_length=100, unique=True)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField(blank=True)
    
    def __str__(self):
        return self.full_name
