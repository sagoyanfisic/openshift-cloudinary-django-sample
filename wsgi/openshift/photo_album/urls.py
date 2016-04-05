from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
import views 


urlpatterns = patterns('',
    # Examples:
    #url(r'^', 'views.home', name='home'),
    url(r'^$', views.list),
    url(r'^list$', views.list),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
