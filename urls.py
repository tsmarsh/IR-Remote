from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', 'AppleRemote.remote.views.index'),
	(r'^frontrow$', 'AppleRemote.remote.views.frontrow'),
	(r'^menu$', 'AppleRemote.remote.views.menu'),
	(r'^back$', 'AppleRemote.remote.views.back'),
	(r'^up$', 'AppleRemote.remote.views.up'),
	(r'^down$', 'AppleRemote.remote.views.down'),
	(r'^left$', 'AppleRemote.remote.views.left'),
	(r'^right$', 'AppleRemote.remote.views.right'),
	(r'^static/(?P<path>.*)$', 'django.views.static.serve',
	        {'document_root': 'remote/static'})
)
