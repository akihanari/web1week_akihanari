from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
# from django.contrib.auth import views
import django.contrib.auth.views
from .views import login_func, logout_func
from . import views

urlpatterns = [
    path('', include('social_django.urls', namespace = 'social')),
    # path('login/',
    #         django.contrib.auth.views.login,
    #         {
    #             'template_name': 'login/index.html',
    #         },
    #         name='login'),
    path('login/', login_func, name="login"),
    path('logout/', logout_func, name="logout"),
    # path('logout/',
    #     django.contrib.auth.views.logout,
    #     {
    #         'template_name': 'logout/index.html',
    #     },
    #     name='logout'),
    path('top/', views.top_page, name="top_page"),

]
