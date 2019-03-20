from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django import forms



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


    username = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
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


    @classmethod
    def get_all_projects(cls):
        projects = cls.objects.all()
        return projects

    @classmethod
    def get_category(cls):
        projects = cls.objects.filter()
        return projects

    @classmethod
    def get_user_projects(cls,user_id):
        projects = cls.objects.filter(username=user_id)
        return projects

    @classmethod
    def project_by_id(cls,id):
        project = cls.objects.filter(id=id)
        return project

    @classmethod
    def search_projects(cls, search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects

    
class Profile(models.Model):
    '''creates instances of user profiles
    
    Arguments:
        models {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''

    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    avatar = models.ImageField(upload_to='avatar/', null=True)
    bio = models.TextField(max_length=255)
    project = models.ForeignKey(Project,on_delete=models.CASCADE, null=True)
    email = models.EmailField()


    def __str__(self):
        return self.username

    def save_profile(self):
        self.save()

    def delete__profile(self):
        self.delete()

    @classmethod
    def get_user_profile(cls,user_id):
        user_profile = cls.objects.filter(user=user_id)
        return user_profile

    
    
   

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
    overall_score = models.DecimalField(decimal_places=2, max_digits=20,blank=True,default=0)
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




    
  







