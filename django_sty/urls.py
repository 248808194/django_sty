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

urlpatterns = [
    # url('cmdb',include('cmdb.urls')),
    url('hmm',include('hmm.urls')),
    url('ormm',include('ormm.urls')),
    url('a',include('a.urls')),
    url('m2m',include('m2m.urls')),
]
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     url('index/(?P<nid>\d+)/(?P<pid>\d+)', views.index,name='indexx'),
#     # url('asdfsadf-(\d+).html', views.detail,name='detail'),
#     # url('detail-(?P<nid>\d+)-(?P<uid>\d+).html',views.detail)
#     # path('login',views.Home.as_view())
# ]
