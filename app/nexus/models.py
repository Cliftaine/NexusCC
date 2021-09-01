from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser ):
    name= models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255, unique=True)
    password= models.CharField(max_length = 255)
    username= models.CharField(max_length = 255)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS=[]

class Team(models.Model):
    #Team name
    name = models.CharField(max_length = 255)

class Accounts(models.Model):
    #
    accountName= models.CharField(max_length = 255)
    #Client Name
    clientName= models.CharField(max_length= 255)
    #Person in charge of operation
    iCOperation= models.CharField(max_length= 255)
    #Team
    team = models.ForeignKey(Team, on_delete=models.CASCADE)


class Movements(models.Model):
    start = models.DateField(auto_now=False, auto_now_add=False)
    end = models.DateField(auto_now=False, auto_now_add=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)



