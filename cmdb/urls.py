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
from django.conf.urls import url
from cmdb import  views

urlpatterns = [
    url('login',views.login),
    url('index',views.index),
    url('user_info',views.user_info),
    url('user_detail-(?P<nid>\d+)',views.user_detail),
    url('user_del-(?P<nid>\d+)',views.user_del),
    url('user_edit-(?P<nid>\d+)',views.user_edit),
    url('user_group',views.user_group),


]
# urlpatterns = [
# url('detail', views.detail),
# url('orm', views.orm),
#     path('admin/', admin.site.urls),
#     url('index/(?P<nid>\d+)/(?P<pid>\d+)', views.index,name='indexx'),
#     # url('asdfsadf-(\d+).html', views.detail,name='detail'),
#     # url('detail-(?P<nid>\d+)-(?P<uid>\d+).html',views.detail)
#     # path('login',views.Home.as_view())
# ]
