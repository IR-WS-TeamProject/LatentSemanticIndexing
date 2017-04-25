"""
	This module provides a server, which can deliver a webapp
	and trigger the search algorithm for an arbitrary query
	(based on the latent semantic indexing method).
"""

#from os import curdir, sep
import urllib
import json
import http.server
import socketserver
from ..lsi.lsi_handler import LSIHandler

PORT = 8000

class MyHandler(http.server.BaseHTTPRequestHandler):
    """Request Handler for the server"""
    def do_HEAD(self):
        """Check if server is running"""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
    def do_GET(self):
        """Get webapp, documents and request api to retrieve ranked list"""
        print("self.path", self.path)
        if self.path == '/':
            path = './src/ui/dist/index.html'
            contenttype = 'text/html'
            print("path: ", path)
            file = open(path, 'rb')
            self.send_response(200)
            self.send_header('Content-type', contenttype)
            self.end_headers()
            self.wfile.write(file.read())
            file.close()
        elif self.path.startswith('/api?query='):
            query = self.path.replace('/api?query=', '')
            query = urllib.parse.unquote(query)
            print('query: ', query)
            lsi_handler = LSIHandler()
            ranked_list = lsi_handler.get_ranking_2(query)
            contenttype = 'application/json'
            body = json.dumps(ranked_list)
            self.send_response(200)
            self.send_header('Content-type', contenttype)
            self.end_headers()
            self.wfile.write(bytearray(body, 'utf-8'))
        elif self.path.startswith('/api?doc='):
            doc = self.path.replace('/api?doc=', '')
            path = './data/20news-bydate/20news-bydate-train/' + doc
            contenttype = 'text/plain'
            print("path: ", path)
            file = open(path, 'rb')
            self.send_response(200)
            self.send_header('Content-type', contenttype)
            self.end_headers()
            self.wfile.write(file.read())
            file.close()
        else:
            path = './src/ui/dist' + self.path
            contenttype = 'application/javascript'
            print("path: ", path)
            file = open(path, 'rb')
            self.send_response(200)
            self.send_header('Content-type', contenttype)
            self.end_headers()
            self.wfile.write(file.read())
            file.close()
        return

def run():
    """Start the server"""
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()
