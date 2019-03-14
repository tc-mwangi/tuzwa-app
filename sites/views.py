from django.http  import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
import datetime as dt
from django.contrib.auth.decorators import login_required


def all_submissions(request):
    '''[summary]
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''



    return render(request, 'projects/all_submissions.html', {})


def submission_details(request):
    '''[summary]
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''



    return render(request, 'projects/submission_details.html', {})


def vote_page(request):
    '''[summary]
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''



    return render(request, 'projects/vote_page', {})


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


def user_profile(request):
    '''[summary]
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''



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


def following(request):
    '''[summary]
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''



    return render(request, 'projects/following.html', {})


def follower(request):
    '''[summary]
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''



    return render(request, 'projects/follower.html', {})


def test(request):
    '''[summary]
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''



    return render(request, 'projects/test.html', {})






    
  
