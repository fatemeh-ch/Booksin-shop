from django.shortcuts import render,get_object_or_404
from blog.models import Post
# Create your views here.


def blog_home_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, 'blog/blog_home.html', context)

def blog_single_view(request,pid):
    posts = Post.objects.filter(status=1)
    post=get_object_or_404(posts,pk=pid)
    return render(request,'blog/blog_single.html',context={'post':post})
