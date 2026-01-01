from django.db import models
from django.contrib.auth.models import User


# Class of categories
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Class of posts
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    # category
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)
