from django.shortcuts import render_to_response
from appscript import *

def index(request):
	return render_to_response('remote.xhtml', mimetype='application/xhtml+xml')

def frontrow(request):
	app(u'System Events').key_code(53, using=k.command_down)
	return render_to_response('remote.xhtml', mimetype='application/xhtml+xml')
	
def play(request):
	app(u'System Events').key_code(36)
	return render_to_response('remote.xhtml', mimetype='application/xhtml+xml')

def menu(request):
	app(u'System Events').key_code(53)
	return render_to_response('remote.xhtml', mimetype='application/xhtml+xml')

def up(request):
	app(u'System Events').key_code(126)
	return render_to_response('remote.xhtml', mimetype='application/xhtml+xml')
			
def down(request):
	app(u'System Events').key_code(125)
	return render_to_response('remote.xhtml', mimetype='application/xhtml+xml')
	
def skip_back(request):
	app(u'System Events').key_code(123)
	return render_to_response('remote.xhtml', mimetype='application/xhtml+xml')

def skip_forward(request):
	app(u'System Events').key_code(124)
	return render_to_response('remote.xhtml', mimetype='application/xhtml+xml')