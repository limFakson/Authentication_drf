from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=130)
    email = models.EmailField(max_length=240)
    phone = models.IntegerField()
    password = models.CharField(max_length=236)
    

# class Login(models.Model):
#     name = model.CharField(max_length=130)
#     password = model.CharField(max_length=8)