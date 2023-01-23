from django.db import models

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=200)
    age=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    qualification=models.CharField(max_length=200)

