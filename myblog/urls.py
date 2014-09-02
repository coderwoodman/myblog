from django.conf.urls import patterns, include, url
import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'',views.hello),
    url(r'^people/',views.hello),
    url(r'^admin/', include(admin.site.urls)),
)
