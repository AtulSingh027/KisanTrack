from django.db import models
from UserLogin.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    Description = models.TextField(max_length=500)
    Poster = models.ImageField(upload_to='images/', blank=True)
    RentPrice = models.IntegerField(blank=False)
    CATEGORY_CHOICES = [
        ('tractors', 'Tractors'),
        ('tools', 'Farm Tools'),
        ('seeds', 'Seeds'),
        ('fertilizers', 'Fertilizers'),
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='tractors')