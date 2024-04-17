from django.db import models

# Create your models here.

class userData(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Mobile = models.CharField(max_length=15)  # Adjust max_length as needed
    AdhaarCard = models.CharField(max_length=20)  # Adjust max_length as needed
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    Gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"



