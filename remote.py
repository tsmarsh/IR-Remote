import tornado.httpserver
import tornado.ioloop
import tornado.web
import re
import os
import pybonjour

port = 8888

class RemoteHandler(tornado.web.RequestHandler):
	def get(self, control):
		print control
		os.system("osascript applescripts/" + control + ".scpt")
		self.write("OK")
				
class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		self.set_header('Content-type', 'application/xhtml+xml')
		return self.render('remote.xhtml')
		
application = tornado.web.Application([
	(r"/", IndexHandler),
	(r"/favicon\.ico", lambda x, y: None),
	(r"/(.*)", RemoteHandler),
])
	
def main():
	pybonjour.DNSServiceRegister(
						name = 'Apple Remote',
						regtype = '_http._tcp',
						port = port,
						callBack = None,
						txtRecord = pybonjour.TXTRecord({'path': '/'}),)
						
	http_server = tornado.httpserver.HTTPServer(application)
	http_server.listen(port)
	tornado.ioloop.IOLoop.instance().start()
	
if __name__ == '__main__':
	main()