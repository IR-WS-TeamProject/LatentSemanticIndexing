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
    lsi_handler = None

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
            query = self.path.split('&svd=')[0].replace('/api?query=', '')
            query = urllib.parse.unquote(query)
            print('query: ', query)
            use_svd = self.path.split('&')[1].replace('svd=', '')
            if "&count=" in self.path:
                count = int(self.path.split('&')[2].replace('count=', ''))
            else:
                count = 10
            if use_svd == 'true':
                documents, similarities = self.lsi_handler.get_ranking(query, number=count)
            else:
                documents, similarities = self.lsi_handler.get_ranking(query, use_SVD=False, number=count)

            ranked_list = []
            for i in range(0, len(similarities)):
                ranked_list.append({'doc': documents[i], 'rank': "{:.9f}".format(similarities[i])})

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
    lsi_handler = LSIHandler()
    MyHandler.lsi_handler = lsi_handler
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()
