__author__ = 'ranveer'
from django.conf.urls import patterns, include, url
from authentication import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    #url(r'^login', views.authentication, name='login'),
    #url(r'^logout', views.logout, name='logout'),
)
