from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lou.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^cohy/', include('cohy.urls', namespace='cohy')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
