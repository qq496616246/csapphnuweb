"""CSAPPweb URL Configuration

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
from django.conf.urls import url, include

urlpatterns = [
    url(r'^index/', include("MainPage.urls")),
    url(r'^ClassSchedule/', include("ClassSchedule.urls")),
    url(r'^userinfomanagement/', include('Csapphnu.urls')),               #个人信息管理
    url(r'^systemmanagement/',include('SystemManagementFun.urls')), #系统管理
]
