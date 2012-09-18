from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
  url(r'^$', 'paprika.business.views.orders'),
  url(r'^orders/$', 'paprika.business.views.orders'),
  url(r'^orders/current/$', 'paprika.business.views.orders'),
  url(r'^flows/$', 'paprika.business.views.flows'),
  url(r'^account/$', 'paprika.business.views.account'),
)
