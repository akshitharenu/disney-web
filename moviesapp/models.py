from django.db import models

# Create your models here.
class customer(models.Model):
    name=models.CharField(max_length=255)
    phone=models.CharField(max_length=10)
    email=models.EmailField(max_length=255)
    password=models.CharField(max_length=255)
class movie(models.Model):
    title=models.CharField(max_length=250)
    trailer=models.FileField(upload_to='videos')
    
    desc= models.TextField()

class Book(models.Model):
    title=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics')
    desc=models.TextField()