"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls import url

from . import views

"""
I had to do my URL patterns using regex and URL
because when I did it the default django 2.0 way using path
when I clicked one of my links, it would append it to the end of the URL
127.0.0.1:8000/resume/contact and then it wouldn't find the page
because I don't have that URL pattern listed. Never had to worry about that
using regex like in djnago 1.11 so I reverted to the older way
"""

"""
The above is fixed now, just keep it for future reference
path did not work previously because in my base.html I did not use template tags
I used plain resume, which would then append the urls together
"""

urlpatterns = [
    #url(r'^$', views.home, name='home'),
    #url(r'^resume/$', views.resume, name='resume'),
    #url(r'^portfolio/$', views.portfolio, name='portfolio'),
    #url(r'^contact/$', views.contact, name='contact'),
    path('', views.home, name='home'),
    path('resume/', views.resume, name='resume'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('admin/', admin.site.urls),
    path('resume/', include('resume.urls'))
]
