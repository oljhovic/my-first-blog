from django.conf.urls import url
from . import views
from views import current_datetime, hours_ahead, index

urlpatterns = [
    #url(r'^$', views.post_list, name='post_list'),
    url(r'^$', views.index, name='index'),
    url(r'^all_posts/$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url('^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
]