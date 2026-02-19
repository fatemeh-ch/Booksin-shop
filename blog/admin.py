from django.contrib import admin
from blog.models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin


# Post manager
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-Empty'
    list_display = ['title', 'author', 'status', 'created_date']
    fields = ['title', 'content', 'status', 'tags', 'author',
              'counted_views', 'image', 'category', 'published_date']
    list_filter = ('status', 'author')
    ordering = ('-created_date',)
    search_fields = ['title']
    summernote_fields = ['content',]


# Category manager
class CategoryAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ['name', 'image']
    fields = ['name', 'image']
    search_fields = ['name']
    empty_value_display = '-Empty'


# Comment Manager
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ['name', 'subject', 'post', 'approved']
    empty_display_value = 'empty'
    list_filter = ['approved']
    search_fields = ['post', 'email', 'name']



# Registering models
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
