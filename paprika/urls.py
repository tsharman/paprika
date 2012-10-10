from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'paprika.views.index'),
    url(r'^login/', 'paprika.views.signin'),
    url(r'^logout/', 'paprika.views.signout'),
    url(r'^signup/', 'paprika.views.signup'),
    url(r'^bu/', include('paprika.business.urls')),
    url(r'^ajax/', include('paprika.ajax.urls')),
    # Examples:
    # url(r'^$', 'paprika.views.home', name='home'),
    # url(r'^paprika/', include('paprika.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
