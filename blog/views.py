from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
import datetime

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def current_datetime(request):
	now = datetime.datetime.now()
	html = '<html><body> today is %s. </body></html>' % now
	return HttpResponse(html)


