from django.conf.urls import patterns, include, url
import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',views.hello),
    url(r'^people/$',views.hello),
    url(r'^admin/$', include(admin.site.urls)),
    url(r'^people/plus/(\d{1,2})/$', views.plus_time),
)
