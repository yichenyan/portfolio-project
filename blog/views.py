from django.shortcuts import render, get_object_or_404
from . import models

# Create your views here.
def bloghome(request):
	blogs = models.Blog.objects
	return render(request, 'blog/bloghome.html',{"blogs":blogs})

def blog_detail(request,blog_id):
	blog_detail = get_object_or_404(models.Blog,pk=blog_id)
	return render(request, 'blog/blog.html',{"blog":blog_detail})

