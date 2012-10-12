from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
  url(r'^move_stage/', 'paprika.ajax.views.move_stage'),
  url(r'^delete_flow/', 'paprika.ajax.views.delete_flow'),
  url(r'^delete_order/', 'paprika.ajax.views.delete_order'),
)
