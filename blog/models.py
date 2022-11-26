from django.db import models


class User(models.Model):
    username=models.CharField(max_length=40)
    email=models.EmailField(max_length=40)
    password=models.CharField(max_length=40)

# Create your models here.
