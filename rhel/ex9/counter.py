#!/usr/bin/python3
import http.server
counter = 0
class handler(http.server.BaseHTTPRequestHandler):
	def do_GET(s):
		global counter
		s.send_response(200)
		s.send_header('Content-type', 'text/html') 
		s.end_headers()
		s.wfile.write(b'%d\n' % counter)
		counter += 1
server = http.server.HTTPServer(('0.0.0.0', 8088), handler) 
server.serve_forever()
