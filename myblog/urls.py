from django.conf.urls import patterns, include, url
import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',views.index),
    url(r'^about/$',views.about),
    url(r'^admin/$', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',),  
)
