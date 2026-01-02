from django import template
from blog.models import Post, Category

register = template.Library()

@register.inclusion_tag('blog/post-categories.html')
def post_categories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories': cat_dict}
