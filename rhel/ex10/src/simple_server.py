#!/usr/bin/python3
from http.server import HTTPServer, SimpleHTTPRequestHandler
counter = 0
def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    """Entrypoint for python server"""
    server_address = ("0.0.0.0", 8000)
    httpd = server_class(server_address, handler_class)
    print("launching server...")
    httpd.serve_forever()(b'%d\n' % counter)

if __name__ == "__main__":
    run()
