from django.shortcuts import render

# function takes a request and returns a render of the request and the .html
# template that is specified


def post_list(request):
    return render(request, 'blog/post_list.html', {})
