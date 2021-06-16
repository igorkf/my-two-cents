from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=50)  # TODO: relate to Author model
    date = models.DateField()
    tags = models.TextField()  # TODO: relate to Tag model

    def __str__(self):
        return self.title
