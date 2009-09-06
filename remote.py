from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import re
import os
import pybonjour

class RemoteHandler(BaseHTTPRequestHandler):
	
	def render_to_response(self, file, mimetype='text/html'):
		self.send_response(200)
		self.send_header('Content-type', mimetype)
		self.end_headers()
		self.wfile.write(open(file, 'r').read())
	
	def runscript(self, name):
		os.system("osascript applescripts/" + name)
			
	def do_GET(self):
		if re.match(r'^/$', self.path):
			return self.render_to_response('remote.xhtml', mimetype='application/xhtml+xml')
		else:
			match = re.match(r'^/(.*)', self.path)
			if match:
				self.runscript(match.group(1) + ".scpt")
				return self.render_to_response('200.html')
	
def main():
	port = 8888
	pybonjour.DNSServiceRegister(
						name = 'Apple Remote',
						regtype = '_http._tcp',
						port = port,
						callBack = None,
						txtRecord = pybonjour.TXTRecord({'path': '/'}),)
					
	try:
		server = HTTPServer(('', port), RemoteHandler)
		print 'started server...'
		server.serve_forever()
		
	except KeyboardInterrupt:
		print 'Received interrupt, shutting down'
		server.socket.close()
	
if __name__ == '__main__':
	main()