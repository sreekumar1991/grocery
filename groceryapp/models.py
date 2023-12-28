from django.db import models

# Create your models here.

class userData(models.Model):
    UserName = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    