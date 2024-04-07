from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  
    password = models.CharField(max_length=100) 
    referral_code = models.CharField(max_length=100, null=True, blank=True)
    code=models.CharField(max_length=100, null=True, blank=True)
    points = models.IntegerField(default=0) 
    timestamp = models.DateTimeField(auto_now_add=True)


class Referral(models.Model):
    referrer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='referrals')
    referred_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='referred_users')
    timestamp = models.DateTimeField(auto_now_add=True)
