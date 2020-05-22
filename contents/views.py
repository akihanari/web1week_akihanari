from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# @login_required
# def private(request):

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
