from django.shortcuts import render
from blog.models import Post
# Create your views here.


def blog_home_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, 'blog/blog_home.html', context)

def blog_single_view(request):
    return render(request,'blog/blog_single.html')
