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
from django.contrib.auth import views as auth_views
from django.urls import  path
from . import views
from users import views as user_views

urlpatterns = [
    path('', views.index, name='user_index'),
    path('profile/', user_views.profile, name='profile'),
    path('contact_page',views.contact_page,name='contact_page'),
    path('cr_account/', views.cr_account, name='cr_account'),
    path('register/', user_views.register, name='register'),
    path('profile/update', views.profile_update, name='profile_update'),
    path('password', views.password_update, name='password'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('favorites/<int:id>', views.add_to_favorites, name='favorites'),
]
