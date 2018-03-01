from django.shortcuts import render
from .models import Post
from django.utils import timezone

# function takes a request and returns a render of the request and the .html
# template that is specified


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
