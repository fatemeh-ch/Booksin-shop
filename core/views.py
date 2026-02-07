from django.shortcuts import render
from blog.models import Category
from core.models import Author, Book

# Create your views here.


# Primary page

def index_view(request):

    categories = Category.objects.all()
    books = Book.objects.all()
    authors = Author.objects.all()

    context = {'categories': categories, 'books': books, 'authors': authors}

    return render(request, 'index.html', context)


def contact_view(request):
    return render(request, 'contact.html')


def about_view(request):
    return render(request, 'about.html')
