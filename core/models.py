from django.db import models

# Create your models here.

#Author
class Author(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='authors/',
                              default='authors/default.png')

# Book
class Book(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='books/', default='books/default.jpg')
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
