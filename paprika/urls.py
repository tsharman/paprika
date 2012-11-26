from django.conf.urls import patterns, include, url
from django.contrib import admin
from paprika.api.orders import *
from paprika.api.orderfeed import *
from tastypie.api import Api
#import settings
admin.autodiscover()
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(BusinessProfileResource())
v1_api.register(OrderFeedResource())


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'paprika.customer.views.search'),
    url(r'^business/', 'paprika.views.index'),
    url(r'^login/', 'paprika.views.signin'),
    url(r'^logout/', 'paprika.views.signout'),
    url(r'^signup/', 'paprika.views.signup'),
    url(r'^bu/', include('paprika.business.urls')),
    url(r'^cu/', include('paprika.customer.urls')),
    url(r'^ajax/', include('paprika.ajax.urls')),
    url(r'^dash/', 'paprika.views.dash'),
    url(r'^api/', include(v1_api.urls)),
    url(r'^investors/', 'paprika.views.investors')
)
