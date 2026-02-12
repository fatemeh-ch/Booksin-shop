from django.contrib import admin
from core.models import Author, Book, Contact


# Book manager
class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-Empty'
    list_display = ['name', 'author', 'created_date']
    fields = ['name', 'description', 'category',
              'author', 'image', 'is_best_sell']
    filter = ['author']
    list_filter = ('author',)
    ordering = ('-created_date',)
    search_fields = ['name', 'author__name']


# Author manager
class AuthorAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ['name', 'image']
    fields = ['name', 'image']
    search_fields = ['name',]
    ordering = ('-created_date',)


# Contact Forms manager
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = 'Empty'
    list_display = ['name', 'subject', 'email']
    fields = ['name', 'subject', 'email', 'message']
    search_fields = ['email', 'name']


# Registering models
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Contact, ContactAdmin)
