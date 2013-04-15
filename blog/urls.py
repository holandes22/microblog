from django.conf.urls import patterns, include, url

from blog.views import post_list, post_detail


urlpatterns = patterns('',
    url(r'^$', post_list, name='list'),
    url(r'^(?P<pk>\d+)/$', post_detail, name='detail'),
)
