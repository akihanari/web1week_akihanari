from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth


def login_func(request):
    return render(request, "registration/index.html")


def logout_func(request):
    return render(request, "logout/logout.html")

# def index_func(request):
#     return render(request, "contents/top.html")


@login_required
def top_page(request):
    user = UserSocialAuth.objects.get(user_id=request.user.id)
    pageDic = {
        'hoge': 'fuga',
        'user': user
    }
    return render(request, 'top/top.html', pageDic)
