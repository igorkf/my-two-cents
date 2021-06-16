from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='author')
    date = models.DateField()
    tags = models.ManyToManyField(Tag, related_name='post_tags')

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField()
    tags = models.ManyToManyField(Tag, related_name='project_tags')

    def __str__(self):
        return self.title
