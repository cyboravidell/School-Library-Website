from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.staff, name="staff"),
    path('/edit_home', views.edit_home, name="edit_home"),
    path('/editAboutCourosel', views.edit_aboutCorousel, name="editAboutCourosel"),
    path('/deleteAboutCorousel', views.delete_about_corousel, name="deleteAboutCorousel"),
    
]
