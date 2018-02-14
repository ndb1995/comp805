from django.contrib import admin
from django.urls import path, re_path

from django.conf.urls import url

from . import views

"""
app name needs to be declared here in order to work with the name space declared in portfolio.urls.py
"""
app_name = "resume"

urlpatterns = [
    path('', views.display_experience_education, name='index'),
]
