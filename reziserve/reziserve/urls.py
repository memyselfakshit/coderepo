"""reziserve URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from pingip import urls, views
from django.views.generic import DetailView,ListView,CreateView,TemplateView

urlpatterns = [
    url(r'^pingip/', include('pingip.urls', namespace="pingip")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index$', views.index, name="index"),
    url(r'^$', views.home, name="home"),
    url(r'^(?P<key>\d+)/(?P<serv>[stc])$', views.indexi),
    url(r'^(?P<key>\d+)/(t)$', views.indexi),
    url(r'^(?P<key>\d+)/(c)$', views.indexi),
    url(r'^(?P<value>\d+)/(?P<serv>[stc])/(?P<key>[A-Za-z]+)/$', views.index),



]
