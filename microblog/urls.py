from django.conf.urls import patterns, include, url
from django.contrib import admin

from microblog.settings.base import STATIC_ROOT
from microblog.views import HomePageView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^posts/', include('blog.urls', namespace='posts')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
                       (r'static/(.*)', 'django.views.static.serve',
                        {'document_root': STATIC_ROOT})
                      )
