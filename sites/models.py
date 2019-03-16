from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django import forms
from tinymce.models import HTMLField


class Category(models.Model):
    '''create instances of project categories
    
    Arguments:
        models {[type]} -- [description]
    '''

    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()



class Country(models.Model):
    '''create instances of project categories
    
    Arguments:
        models {[type]} -- [description]
    '''

    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

    def save_country(self):
        self.save()

    def delete_country(self):
        self.delete()

   


class Project(models.Model):
    '''creates instances of projects
    
    Arguments:
        models {[type]} -- [description]
    '''


    username = models.ForeignKey(User,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar/',null=True)
    title = models.CharField(max_length=255)
    screenshot = models.ImageField(upload_to='screenshot/') 
    description = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    published_date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)


    def __str__(self):
        return self.title


    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()
    
    
class Profile(models.Model):
    '''creates instances of user profiles
    
    Arguments:
        models {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''

    username = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    avatar = models.ImageField(upload_to='avatar/')
    bio = models.TextField(max_length=255)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    email = models.EmailField()


    def __str__(self):
        return self.username

    def save_profile(self):
        self.save()

    def delete__profile(self):
        self.delete()
    
   

class Rating(models.Model):
    '''creates rating instances
    
    Arguments:
        models {[type]} -- [description]
    '''


    nominee = models.ForeignKey(User,on_delete=models.CASCADE)
    design = models.IntegerField(blank=True,default=0)
    usability = models.IntegerField(blank=True,default=0)
    creativity = models.IntegerField(blank=True,default=0)
    content = models.IntegerField(blank=True,default=0)
    overall_score = models.IntegerField(blank=True,default=0)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
   

    def __str__(self):
        return self.nominee

    
    def save_rating(self):
        self.save()

    def delete__rating(self):
        self.delete()


class Follow(models.Model):
    '''creates instances of followers and following
    
    Arguments:
        models {[type]} -- [description]
    '''

    follower = models.ForeignKey(User, related_name='+', null=True)
    following = models.ForeignKey(User,related_name='+', null=True)




    
  







