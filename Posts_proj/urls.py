"""Posts_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from Posts_App import views
from django.urls import include, path
from Posts_App import api


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name='home_name'),
    path('login/', views.login_view, name='login_name'),
    path('register/', views.register_view, name='register_name'),
    path('time_line/', views.time_ine_view, name='time_line_name'),
    path('profile/', views.profile_view, name = 'profile_name'),
    path('add_post/',views.add_post_view,name= 'add_post_name'),
    path('',include('Posts_App.urls'))


]
