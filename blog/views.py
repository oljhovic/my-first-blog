from django.shortcuts import render
from django.http import HttpResponse, Http404
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


def index(request):
	return render(request, 'blog/base.html')






def current_datetime(request):
	now = datetime.datetime.now()
	html = '<html><body> today is %s. </body></html>' % now
	return HttpResponse(html)

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = '<html><body> cherez %s chasov budet %s. </body></html>' % (offset, dt)
	return HttpResponse(html)



