from django.contrib import admin

from .models import Post, Author, Tag, Project, Job

# Register your models here.


admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Project)
admin.site.register(Job)
