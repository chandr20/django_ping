"""ping_test_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from ping_test.views import (
Serverlist,
IpListView,
Ipaction,Reset,
JobStatus,Dellist
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^server_ips/',Serverlist.as_view(),name='serverlist'),
    url(r'^Iplist/$',IpListView.as_view()),
    url(r'^(?P<pk>\d+)/$',Ipaction.as_view(),name='ip-action'),
    url(r'^reset/(?P<pk>\d+)/$',Reset.as_view(),name='ip-del'),
    url(r'^job/(?P<job>[a-f0-9-]+)/$',JobStatus.as_view(),name='ip-job'),
    url(r'^Iplist/del_list/(?P<pk>\d+)/$',Dellist.as_view(),name='dellist'),

]
