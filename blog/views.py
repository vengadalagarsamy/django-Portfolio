from django.shortcuts import render, get_object_or_404
from .models import Blogpost

def all_blogs(request):
    blogposts = Blogpost.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blogposts':blogposts})

def detail(request, blog_id):
    blog = get_object_or_404(Blogpost, pk=blog_id)
    return render(request, 'blog/detail.html', {'post':blog})
