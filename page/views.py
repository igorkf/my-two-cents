from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'page/index.html')


def who_am_i(request):
    return HttpResponse('Who am I?')


def posts(request):
    return HttpResponse('Posts')


def projects(requests):
    return HttpResponse('Projects')
