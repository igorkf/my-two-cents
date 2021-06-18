from datetime import date

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView

from . import models

# Create your views here.


class IndexView(TemplateView):
    template_name = 'page/index.html'


class JobsView(ListView):
    model = models.Job
    template_name = 'page/who-am-i.html'
    context_object_name = 'jobs'


class PostsView(ListView):
    model = models.Post
    template_name = 'page/posts.html'
    context_object_name = 'posts'


class ProjectsView(ListView):
    model = models.Project
    template_name = 'page/projects.html'
    context_object_name = 'projects'