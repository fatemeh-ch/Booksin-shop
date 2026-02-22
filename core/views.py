from django.shortcuts import render, redirect
from django.db.models import Count
from blog.models import Category
from core.models import Author, Book
from core.forms import ContactForm
from django.contrib import messages

# Create your views here.


# Home page view
def index_view(request):

    categories = Category.objects.all()
    books = Book.objects.all()
    authors = Author.objects.annotate(book_count=Count('book'))

    context = {'categories': categories, 'books': books, 'authors': authors}

    return render(request, 'index.html', context)


# Contact page view
def contact_view(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Your message was recieved successfully')
            return redirect('core:contact')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Your message was not sent!')

    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)


# About us page view
def about_view(request):
    return render(request, 'about.html')
