"""django_sty URL Configuration

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
from django.urls import path
from django.conf.urls import url,include
from hmm import  views

urlpatterns = [
url('login',views.login),
url('ttt',views.ttt),
url('index',views.index),
url('user_info',views.userinfo),
url('user_group',views.usergroup),
url('group_del-(?P<gid>\d+)',views.group_del),
url('user_del-(?P<uid>\d+)',views.user_del),
url('user_edit-(?P<uid>\d+)',views.user_edit),
]