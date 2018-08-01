#!/usr/bin/python

from http.server import BaseHTTPRequestHandler, HTTPServer

PORT_NUMBER = 8080

class MyHandler(BaseHTTPRequestHandler):

  def do_GET(self):
    """Handler for GET requests"""
    self.send_response(200)
    self.send_header('Content-type','text/html')
    self.end_headers()

    print(self.wfile)

    content = "<html><body><p>This is my awesome app.</p></body></html>"
    self.wfile.write(bytes(content, 'utf-8'))
    self.wfile.close()
    """
    with open('logo.png', 'rb') as f:
      self.wfile.write(f.read())
    """

try:
  server = HTTPServer(('', PORT_NUMBER), MyHandler)
  print('Started httpserver on port', PORT_NUMBER)
  server.serve_forever()

except KeyboardInterrupt:
  server.server_close()
  print('Stopping server')
