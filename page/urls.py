from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('who-am-i', views.who_am_i, name='who-am-i'),
    path('posts', views.posts, name='posts'),
    path('projects', views.projects, name='projects')
]
