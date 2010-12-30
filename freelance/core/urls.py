from django.conf.urls.defaults import *

urlpatterns = patterns('freelance.core.views',
		url(r'^$', 'index', name='index'),
		url(r'^contact_form/$', 'contact_form', name='contact_form'),
		url(r'^portfolio/$', 'portfolio', name='portfolio'),
		url(r'^tag/(?P<tag>.*)/$', 'tag', name='tag'),
)
