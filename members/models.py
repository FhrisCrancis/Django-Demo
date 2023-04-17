from django.db import models

# Create your models here.

#refer to djando model documentation, this allow us to make db tables based on models
#by default django generates an id field to use as primary key unless you specify

#changes here and in admin.py require makemigration and migrate commands
class Member(models.Model):
    firstname = models.CharField(max_length=20, null=True)
    lastname = models.CharField(max_length=20, null=True)
    doj = models.DateField(null=True)
    
    def __str__(self):
        return self.firstname + " " + self.lastname
    

