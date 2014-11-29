from django.conf.urls import patterns, url


urlpatterns = patterns('tempcontrol.views',
    url(r'^$', 'home'),
    url(r'^gettemp/$', 'get_temperature'),
)
