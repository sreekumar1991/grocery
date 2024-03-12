from django.db import models

# Create your models here.

class userData(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Mobile = models.CharField(max_length=10)
    AdhaarCard = models.IntegerField(default=0)









