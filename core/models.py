from django.db import models
from blog.models import Category

# Create your models here.

#Author
class Author(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='authors/',
                              default='authors/default.png')
    
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name.title()


# Book
class Book(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='books/', default='books/default.jpg')
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    is_best_sell=models.BooleanField(default=False)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL, null=True)

    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
