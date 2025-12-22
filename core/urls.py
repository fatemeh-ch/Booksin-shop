from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name='home'),
    path('contact',contact_view, name='contact')
]

app_name='core'