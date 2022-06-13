from operator import mod
from secrets import choice
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='products/photos/')
    rental_period = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


class Review(models.Model):
    comment = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
