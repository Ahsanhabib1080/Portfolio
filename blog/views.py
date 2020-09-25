from django.shortcuts import render, get_object_or_404
from .models import Blog
# render will always return from inside templates folder
def all_blogs(request):
    blog_count = Blog.objects.count
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blogs': blogs,'blog_count':blog_count})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})