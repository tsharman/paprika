from django.conf.urls import patterns, url

urlpatterns = patterns('',
  url(r'^$', 'paprika.customer.views.search'),
  url(r'^search/$', 'paprika.customer.views.search'),
)
