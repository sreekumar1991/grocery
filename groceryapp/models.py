from django.db import models

# Create your models here.

class userData(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    PanCard = models.CharField(max_length=10)
    AdhaarCard = models.IntegerField(default=0)
    Password = models.CharField(max_length=100)
    Confirm_Password = models.CharField(max_length=100)








