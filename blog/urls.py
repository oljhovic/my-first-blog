from django.conf.urls import url
from . import views


urlpatterns = [
    #url(r'^$', views.post_list, name='post_list'),
    url(r'^$', views.index, name='index'),
    url(r'^about_me/$', views.about_me, name='about_me'),
    url(r'^portfolio/$', views.portfolio, name='portfolio'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^all_posts/$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    
]