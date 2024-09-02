from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    text = models.TextField(max_length=240)
    photo = models.ImageField(upload_to='photos/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.text[:10]}'
    
class contact(models.Model):
    name = models.CharField(max_length=20)
    message = models.TextField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.name}'

