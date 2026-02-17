from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from blog.models import Post
from taggit.models import Tag


# Queries
tags=Tag.objects.all()


# Views

def blog_home_view(request,**kwargs):
    posts = Post.objects.filter(status=1)
    
    if kwargs.get('cat_name')!=None:
        posts=Post.objects.filter(category__name=kwargs['cat_name'])

    if kwargs.get('author_name')!=None:
        posts=Post.objects.filter(author__username=kwargs['author'])

    if kwargs.get('tag_name')!=None:
        posts=Post.objects.filter(tags__name__in=[kwargs['tag_name']])

    paginator=Paginator(posts,3)
    
    try:
        page_number=request.GET.get('page')
        posts=paginator.get_page(page_number)

    except EmptyPage:
        posts=paginator.get_page(1)

    except PageNotAnInteger:
        posts=paginator.get_page(1)


    context = {'posts': posts,'tags':tags}
    return render(request, 'blog/blog_home.html', context)

def blog_single_view(request,pid):
    posts = Post.objects.filter(status=1)
    post=get_object_or_404(posts,pk=pid)

    tags=post.tags.all()

    context={'post':post,'tags':tags}
    return render(request,'blog/blog_single.html',context)

def blog_search_view(request):
    posts = Post.objects.filter(status=1)
    if request.method=='GET':
        posts=posts.filter(content__contains=request.GET.get('s'))
    context={'posts':posts}
    return render(request,'blog/blog_home.html',context)
    