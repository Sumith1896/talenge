__author__ = 'ranveer'
from django.conf.urls import patterns, include, url
from student import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
)
