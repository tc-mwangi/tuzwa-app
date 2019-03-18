from django.http  import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from sites.models import Category, Country, Project, Profile
from django.contrib.auth.decorators import login_required
import datetime as dt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from annoying.functions import get_object_or_None


def all_submissions(request):
    '''displays all submitted projects
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''

    projects = Project.get_all_projects()
    print(projects)


    return render(request, 'projects/all_submissions.html', {"projects":projects})

   

 








def submission_details(request):
    '''[summary]
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''



    return render(request, 'projects/submission_details.html', {})


@login_required(login_url='/accounts/login/')
def vote_page(request):
    '''[summary]
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''



    return render(request, 'projects/vote_page.html', {})


def site_modal(request):
    '''[summary]
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''



    return render(request, 'projects/site_modal.html', {})


def submit_a_site(request):
    '''[summary]
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''



    return render(request, 'projects/submit_a_site.html', {})


def designers(request):
    '''[summary]
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''



    return render(request, 'projects/designers.html', {})


def api(request):
    '''[summary]
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''



    return render(request, 'projects/api.html', {})


@login_required(login_url='/accounts/login/')
def user_profile(request):
    '''[summary]
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''
    
    
    # profile = Profile.objects.all()
    # print(profile)
    # projects = Project.objects.all()
    # print(projects)

    # current_user = request.user
    # profile = Profile.objects.get(username=current_user)
    # print(profile)
    # projects = Project.objects.filter(username=current_user)
    # print(projects)
    


    return render(request, 'projects/user_profile.html', {})



def edit_profile(request):
    '''[summary]
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''



    return render(request, 'projects/edit_profile.html', {})


def search_project(request):
    '''[summary]
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''



    return render(request, 'projects/search_project.html', {})


def following_list(request):
    '''[summary]
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''



    return render(request, 'projects/following_list.html', {})


def follower_list(request):
    '''[summary]
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''



    return render(request, 'projects/follower_list.html', {})


def test_page(request):
    '''[summary]
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''



    return render(request, 'shared/test_page.html', {})


def nominees(request):
    '''[summary]
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''



    return render(request, 'shared/nominees.html', {})

def site_of_the_day(request):
    '''[summary]
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''



    return render(request, 'shared/site_of_the_day.html', {})


def directory(request):
    '''[summary]
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''



    return render(request, 'shared/directory.html', {})


def previous_winners(request):
    '''[summary]
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''



    return render(request, 'shared/previous_winners.html', {})















    
  
