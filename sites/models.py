from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django import forms


class Project(models.Model):
    '''creates instances of projects
    
    Arguments:
        models {[type]} -- [description]
    '''
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

    avatar = models.ImageField(upload_to='avatar/')
    bio = models.TextField(max_length=255)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    screenshot = models.ImageField(upload_to='screenshot/')
    description = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    email = models.EmailField()


    def __str__(self):
        return self.avatar

    







