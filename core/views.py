from django.shortcuts import render
from blog.models import Category

# Create your views here.

# Primary page
def index_view(request):
    
    categories=Category.objects.all()
    context={'categories':categories}

    return render(request, 'index.html',context)


def contact_view(request):
    return render(request, 'contact.html')


def about_view(request):
    return render(request,'about.html')
