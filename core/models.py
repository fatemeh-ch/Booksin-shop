from django.db import models
from blog.models import Category



# Author
class Author(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='authors/',
                              default='authors/default.png')

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name.title()


# Books
class Book(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='books/', default='books/default.jpg')
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    is_best_sell = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name[:30]


# Contact
class Contact(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject[:30]

    class Meta:
        ordering = ('-id',)
