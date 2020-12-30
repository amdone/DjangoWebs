"""PythonWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.conf.urls import url
from django.urls import path, include
from PythonWeb import views
from acfun import toll
from bili import views as bili
from login import views as login
from youtube import views as youtube
from django.contrib import admin
from other import views as other
from twitter import views as twitter

urlpatterns = [
    url(r'^$', views.index),
    url(r'^comments/', include('django_comments.urls')),
    url(r'captcha/', include('captcha.urls')),
    url(r'^admin/', admin.site.urls),
    path('acfun/', include("apps.acfun.urls")),
    path('bili/', bili.bili),
    path('youtube/', youtube.youtube),
    path('index/', views.index),
    # path('test/', views.test),
    path('twitter/', twitter.twitter),
    path('toll/', toll.toll),
    path('toll2/', toll.toll2),
    path('toll-form/', toll.toll_form),
    path('login/', login.login),
    path('register/', login.register),
    path('logout/', login.logout),
    path('profile/', login.profile),
    path('about/', views.about),
    path('twittertools/', views.twittertools),
    path('acfuntools/', views.acfuntools),
    path('bilitools/', views.bilitools),
    path('search/', views.search),
    path('weblog/', views.weblog),
    path('upgrade/', login.upgrade),
    path('level/', other.level),
    path('black/', other.black),
    path('board/', other.board),
    path('recomment/', other.recomment),
]
