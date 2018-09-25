
__author__ = 'keshav'
from django.conf.urls import url

from . import views

urlpatterns = [

        url(r'^Streamers/$', views.index),

    ]