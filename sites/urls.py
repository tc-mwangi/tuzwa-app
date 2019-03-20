from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    url(r'^submissions/$', views.all_submissions, name='all_submissions'),
    url(r'^submission-details/$', views.submission_details, name='submission_details'),
    url(r'^modal/$', views.site_modal, name='site_modal'), 
    url(r'^vote/$', views.vote_page, name='vote_page'),
    url(r'^submit/$', views.submit_a_site, name='submit_a_site'),
    url(r'^designers/$', views.designers, name='designers'),
    url(r'^submit/$', views.api, name='api'),
    url(r'^u/(?P<username>[\w-]+)$', views.user_profile, name='user_view'),  
    url(r'^profile/$', views.user_profile, name='user_profile'),
    url(r'^edit-profile/$', views.edit_profile, name='edit_profile'),
    url(r'^search/$', views.search_project, name='search_project'),   
    url(r'^following/$', views.following_list, name='following_list'),
    url(r'^followers/$', views.follower_list, name='follower_list'), 
    url(r'^api/$', views.api, name='api'),
    url(r'^test/$', views.test_page, name='test_page'),
    url(r'^previous_winners/$', views.previous_winners, name='previous_winners'), 
    url(r'^directory/$', views.directory, name='directory'),
    url(r'^site_of_the_day/$', views.site_of_the_day, name='site_of_the_day'),
    url(r'^nominees/$', views.nominees, name='nominees'),
    url(r'^create_profile/$', views.create_profile, name='create_profile'),
   
]







