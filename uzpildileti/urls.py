from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indexView, name='index'),
    path('login/', views.loginView, name='login'),
    path('register/', views.registerView, name='register'),
    path('favourite/', views.favouriteView, name='favourite'),
    path('about/', views.aboutView, name='about'),
    path('station/', views.stationView, name='station'),
]
