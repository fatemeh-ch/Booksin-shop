from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from blog.models import Post
# Create your views here.


def blog_home_view(request,cat_name=None,author_name=None):
    posts = Post.objects.filter(status=1)
    if cat_name:
        posts=Post.objects.filter(category__name=cat_name)

    if author_name:
        posts=Post.objects.filter(author__username=author_name)

    paginator=Paginator(posts,3)
    try:
        page_number=request.GET.get('page')
        posts=paginator.get_page(page_number)

    except EmptyPage:
        posts=paginator.get_page(1)

    except PageNotAnInteger:
        posts=paginator.get_page(1)


    context = {'posts': posts}
    return render(request, 'blog/blog_home.html', context)

def blog_single_view(request,pid):
    posts = Post.objects.filter(status=1)
    post=get_object_or_404(posts,pk=pid)
    return render(request,'blog/blog_single.html',context={'post':post})

def blog_search_view(request):
    posts = Post.objects.filter(status=1)
    if request.method=='GET':
        posts=posts.filter(content__contains=request.GET.get('s'))
    context={'posts':posts}
    return render(request,'blog/blog_home.html',context)
    