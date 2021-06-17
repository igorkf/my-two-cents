from django.contrib import admin
from django.db import models
from pagedown.widgets import AdminPagedownWidget

from .models import Post, Author, Tag, Tech, Project, Job


# Register your models here.


class PagedownEditorAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }


admin.site.register(Post, PagedownEditorAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Tech)
admin.site.register(Project, PagedownEditorAdmin)
admin.site.register(Job, PagedownEditorAdmin)
