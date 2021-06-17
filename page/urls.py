from django.urls import path

from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('who-am-i', views.JobsView.as_view(), name='who-am-i'),
    path('posts', views.PostsView.as_view(), name='posts'),
    path('projects', views.ProjectsView.as_view(), name='projects')
]
