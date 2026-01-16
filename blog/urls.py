from django.urls import path
from .views import *

urlpatterns=[
    path('',blog_home_view,name='home'),
    path('single/<int:pid>',blog_single_view,name='single'),
    path('category/<str:cat_name>',blog_home_view,name='category'),
    path('author/<str:author_name>',blog_home_view,name='author'),
    path('search/',blog_search_view,name='search')
]

app_name='blog'