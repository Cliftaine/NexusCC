from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser ):
    name= models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50, unique=True)
    password= models.CharField(max_length = 50)
    username=None

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS=[]

class Team(models.Model):
    #Team name
    name = models.CharField(max_length = 50)

class Accounts(models.Model):
    #
    accountName= models.CharField(max_length = 50)
    #Client Name
    clientName= models.CharField(max_length= 50)
    #Person in charge of operation
    iCOperation= models.CharField(max_length= 50)
    #Team
    team = models.ForeignKey(Team, on_delete=models.CASCADE)


class Movements(models.Model):
    start = models.DateField(auto_now=False, auto_now_add=False)
    end = models.DateField(auto_now=False, auto_now_add=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)



