from django.contrib import admin
from blog.models import Post, Category


# Post manager
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-Empty'
    list_display = ['title', 'author', 'status', 'created_date']
    fields = ['title', 'content', 'status', 'author',
              'counted_views', 'image', 'category', 'published_date']
    list_filter = ('status', 'author')
    ordering = ('-created_date',)
    search_fields = ['title']


# Category manager
class CategoryAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ['name', 'image']
    fields = ['name', 'image']
    search_fields = ['name']
    empty_value_display = '-Empty'


# Registering models
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
