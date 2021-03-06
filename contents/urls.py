from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
# from django.contrib.auth import views
import django.contrib.auth.views
from .views import login_func, logout_func, top_page
from . import views

urlpatterns = [
    # path('', include('social_django.urls', namespace = 'social')),
    path('', include('social_django.urls')),
    # path('', views.index_func, name="index"),
    path('', login_func, name="login"),
    path('logout/', logout_func, name="logout"),
    # path('login/', views.login_func, name="login"),
    path('top/', top_page, name="top_page"),

]
