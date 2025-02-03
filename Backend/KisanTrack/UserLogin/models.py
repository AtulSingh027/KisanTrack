from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    Pic = models.ImageField(upload_to='images/UserProfilePic/', blank=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50 ,blank=True)
    phone = models.CharField(max_length=10, blank=True)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    