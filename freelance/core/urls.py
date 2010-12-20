from django.conf.urls.defaults import *

urlpatterns = patterns('freelance.core.views',
		url(r'^$', 'index', name='index'),
)
