from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django import forms


class Project(models.Model):
    '''creates instances of projects
    
    Arguments:
        models {[type]} -- [description]
    '''
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    screenshot = models.ImageField(upload_to='screenshot/')
    description = models.CharField(max_length=255)
    link = models.CharField(max_length=255)


    def __str__(self):
        return self.title

    


class Profile(models.Model):
    '''creates instances of user profiles
    
    Arguments:
        models {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''

    username = models.ForeignKey(User,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar/')
    bio = models.TextField(max_length=255)
    title = models.CharField(max_length=255)
    screenshot = models.ImageField(upload_to='screenshot/')
    description = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    email = models.EmailField()


    def __str__(self):
        return self.title

    







