from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
  url(r'^$', 'paprika.business.views.orders'),
  url(r'^orders/$', 'paprika.business.views.orders', {'order_filter' : 'current'}),
  url(r'^orders/current/', 'paprika.business.views.orders', {'order_filter' : 'current' }),
  url(r'^orders/done/', 'paprika.business.views.orders', { 'order_filter' : 'done' }),
  url(r'^orders/canceled/', 'paprika.business.views.orders', { 'order_filter' : 'canceled'}),
  url(r'^flows/$', 'paprika.business.views.flows'),
  url(r'^account/$', 'paprika.business.views.account'),
)
