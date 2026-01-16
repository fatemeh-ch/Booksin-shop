from django.urls import path
from .views import *

urlpatterns=[
    path('',blog_home_view,name='home'),
    path('single/<int:pid>',blog_single_view,name='single'),
]

app_name='blog'