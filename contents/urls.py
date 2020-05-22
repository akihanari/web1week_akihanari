from django.urls import path

from . import views
import django.contrib.auth.views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
        },
        name='login'),
    url(r'^logout/$',
        django.contrib.auth.views.logout,
        {
            'template_name': 'app/logout.html',
        },
        name='logout'),
    url(r'^private/$', app.views.private, name='private'),
]
