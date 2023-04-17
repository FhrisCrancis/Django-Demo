from django.db import models

# Create your models here.

class Employee(models.Model):
    firstname = models.CharField(max_length=255)
    tech = models.CharField(max_length=20)

    def __str__(self):
        return self.firstname
