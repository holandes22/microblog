from django.shortcuts import render

from blog.models import Post

def post_list(request, *args, **kwargs):
    post_list = Post.objects.filter(published=True)
    template_name = 'post_list.html'
    context = {
        'post_list': post_list,
    }

    return render(request, template_name, context)

def post_detail(request, pk):
    post = Post.objects.get(pk=pk, published=True)
    template_name = 'post_detail.html'
    context = {
        'post': post,
    }

    return render(request, template_name, context)

