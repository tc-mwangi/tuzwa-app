from django.http  import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from sites.models import Category, Country, Project, Profile
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
    current_user = request.user
    form = ProjectForm()


    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.username = current_user
            project.save()
        return HttpResponseRedirect('user_profile')

    else:
        form = ProjectForm()
 
    return render(request, 'projects/submit_a_site.html', {"form": form})




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
    current_user = request.user
    projects = Project.get_user_projects(current_user)
    profile = Profile.get_user_profile(current_user)
    
   


    return render(request, 'projects/user_profile.html', {"projects":projects,"profile":profile})



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



# try:
#         if not request.user.is_authenticated:
#             return redirect('/accounts/login/')
#         current_user = request.user
#         profile =Profile.objects.get(username=current_user)
#         print(current_user)
#     except ObjectDoesNotExist:
#         return redirect('user_profile')



















    
  
