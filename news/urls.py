"""
URL configuration for mftiHW project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import  path
from . import views

urlpatterns = [
    path('all_news/', views.all_news, name='all_news'),
    path('show/', views.index, name='news_index'),
    path('show/<int:id>/', views.news_detail, name='news_detail'),
    path('news_add/', views.news_add, name='news_add'),
    path('addnews/', views.addnews, name='addnews'),
    path('create/', views.add_article, name='create_article'),



]
