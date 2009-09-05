from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', 'AppleRemote.remote.views.index'),
	(r'^frontrow$', 'AppleRemote.remote.views.frontrow'),
	(r'^menu$', 'AppleRemote.remote.views.menu'),
	(r'^play$', 'AppleRemote.remote.views.play'),
	(r'^up$', 'AppleRemote.remote.views.up'),
	(r'^down$', 'AppleRemote.remote.views.down'),
	(r'^skip_back$', 'AppleRemote.remote.views.skip_back'),
	(r'^skip_forward$', 'AppleRemote.remote.views.skip_forward'),
	(r'^static/(?P<path>.*)$', 'django.views.static.serve',
	        {'document_root': 'remote/static'})
)
