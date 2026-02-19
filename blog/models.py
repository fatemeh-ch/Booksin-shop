from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


# Category
class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='categories/',
                              default='categories/default.jpg')

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


# Post
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=0)
    tags = TaggableManager()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.title[:20]

    class Meta:
        ordering = ['-created_date']


# Comment
class Comment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    approved = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']
