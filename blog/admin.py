from django.contrib import admin
from blog.models import Post,Category

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-Empty'
    list_display = ['title', 'author', 'status', 'created_date']
    fields = ['title', 'content', 'status', 'author',
              'counted_views', 'image', 'category', 'published_date']
    list_filter = ('status', 'author')
    ordering = ('-created_date',)
    search_fields = ['title']

admin.site.register(Post,PostAdmin)
admin.site.register(Category)