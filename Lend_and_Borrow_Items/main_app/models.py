from asyncio.windows_events import NULL
from datetime import date
from operator import mod
from re import T
from secrets import choice
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User



class Product(models.Model):
    '''
    Product model
    '''
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    image = models.URLField(null=True)
    rental_period = models.IntegerField(help_text="in days")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class Review(models.Model):
    '''
    Review model
    '''
    RATING_CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    )

    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(null=True, choices=RATING_CHOICES)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



class Profile(models.Model):
    '''
    Profile model
    '''
    name = models.CharField(max_length=64)
    bio = models.TextField(null=True, max_length=1024)
    image = models.URLField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

  
    def __str__(self):
        return self.name