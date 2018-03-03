# from django.conf.urls import path
from django.conf.urls import include, url
from . import views
from django.contrib.auth.views import login, logout
from django.contrib.auth import views as auth_views

# Then dajax urls:

urlpatterns = [
    url(r'^login/$', views.login_user, name='login'),
    # url(r'^logout/$', logout, {'template_name': 'MSR/logout.html'}, name='logout'),
    url(r'^home/$', views.index, name='index'),
    url(r'^search/$', views.searchVideo, name='searchVideo'),
    url(r'^saveComments/$', views.saveComments, name='saveComments'),
    url(r'^rawVideos/$', views.rawVideos, name='rawVideos'),
    url(r'^m1Videos/$', views.m1Videos, name='m1Videos'),
    url(r'^addVideos/$', views.addVideos, name='addVideos'),
    url(r'^addM1Videos/$', views.m1Done, name='m1Done'),
]

# urlpatterns += patterns('',
#    url(r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),)
	
# urlpatterns += staticfiles_urlpatterns()