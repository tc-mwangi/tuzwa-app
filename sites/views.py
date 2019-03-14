from django.shortcuts import render



def all_submissions(request):


    return render(request, '', {})




  url(r'^$', views.all_submissions, name='all_submissions'),
    url(r'^$', views.submission_page, name='submission_page'),
    url(r'^$', views.site_modal, name='site_modal'), 
    url(r'^$', views.vote_page, name='vote_page'),
    url(r'^submit/$', views.submit_a_site, name='submit_a_site'),
    url(r'^designers/$', views.designers, name='designers'),
    url(r'^submit/$', views.api, name='api'),
    url(r'^u/(?P<username>[\w-]+)$', views.user_profile, name='user_view'),  
    url(r'^profile/$', views.user_profile, name='user_profile'),
    url(r'^profile/edit$', views.edit_profile, name='edit_profile'),
    url(r'^search/$', views.search_projects, name='search_projects'),   
    url(r'^following/$', views.following, name='following'),
    url(r'^followers/$', views.follower, name='follower'), 
    url(r'^test/$', views.test, name='test'),
