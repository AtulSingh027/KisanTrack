from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # pic = models.ImageField(upload_to='images/UserProfilePic/', blank=True)
    # phone = models.CharField(max_length=10, blank=True)
    # address = models.TextField(blank=True)
    # city = models.CharField(max_length=50, blank=True)
    # state = models.CharField(max_length=50, blank=True)

class OTPModel(models.Model):
    email = models.EmailField()
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.email} - {self.otp} - {self.created_at}"
