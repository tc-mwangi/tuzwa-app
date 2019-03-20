from django.http  import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from sites.models import Category, Country, Project, Profile, Rating
from django.contrib.auth.decorators import login_required
import datetime as dt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from annoying.functions import get_object_or_None
from django.core.exceptions import ObjectDoesNotExist
from .forms import ProfileForm, ProjectForm, RatingForm


def all_submissions(request):
    '''displays all submitted projects
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''
    date = dt.date.today()

    projects = Project.get_all_projects()
    print(projects)

    current_user = request.user
    # profile = Profile.objects.get(username=current_user)
    # print(profile)


    return render(request, 'projects/all_submissions.html', {"projects":projects})


def search_project(request):
    '''[summary]
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''
    if 'project' in request.GET and request.GET["project"]:
        projects = Project.search_projects(search_term)
        message = f"{search_term}"

        return render(request, 'projects/search_project.html', {"message":message, "projects":projects})

    else:
        message = "You haven't saerched for a project"
        
        return render(request, 'projects/all_submissions.html', {"message":message, "projects":projects})


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


@login_required(login_url='/accounts/login/')
def submit_a_site(request):
    '''[summary]
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''
    current_user = request.user
    form = ProjectForm()


    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            
            
        return redirect('user_profile')
        # message = "Your site has been posted"

    else:
        form = ProjectForm()
 
    return render(request, 'projects/submit_a_site.html', {"form": form})


@login_required(login_url='/accounts/login/')
def user_profile(request, username=None):
    '''[summary]
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''
    form = ProfileForm

    if username is None:
        user =request.user
    else:
        user = User.objects.get(username=username)
    
    projects = Project.objects.filter(username=user.id)

    profile = Profile.objects.filter(user=user.id)
    
    return render(request, 'projects/user_profile.html', {"projects":projects,"profile":profile, "form":form})


   
    

def edit_profile(request):
    '''[summary]
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''



    return render(request, 'projects/edit_profile.html', {})






def designers(request):
    '''[summary]
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''



    return render(request, 'projects/designers.html', {})


def api(request):
    '''display api page and data
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''



    return render(request, 'projects/api.html', {})




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


def previous_winners(request):
    '''[summary]
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''



    return render(request, 'shared/previous_winners.html', {})

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


@login_required(login_url='/accounts/login/')
def create_profile(request):
    '''[summary]
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''
    current_user = request.user
    if request.method=='POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = current_user

            profile.save()
        return redirect('user_profile')
    else:
        form=ProfileForm()

    return render(request, 'projects/create_profile.html', {"form":form})





















    
  
