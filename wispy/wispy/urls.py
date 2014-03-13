from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', 'clusters.views.home', name='home'),
                       url(r'^virtual_environments/(\d+)/$',
                           'clusters.views.virtual_environment_detail',
                           name='virtual_environment_detail'
                           ),
                       url(r'^clusters/(\d+)/$',
                           'clusters.views.cluster_detail',
                           name='cluster_detail'),
                       )
