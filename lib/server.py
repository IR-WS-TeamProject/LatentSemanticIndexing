import http.server
import socketserver
from os import curdir, sep
import urllib
import json

import queryexec

#https://docs.python.org/3/library/http.server.html

PORT = 8000

class MyHandler(http.server.BaseHTTPRequestHandler):
	def do_HEAD(s):
		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()
	def do_GET(self):
		print("self.path", self.path)
		if self.path == '/':
			path = './ui/dist/index.html'
			contenttype = 'text/html'
			print("path: ", path)
			f = f = open(path, 'rb')
			self.send_response(200)
			self.send_header('Content-type',contenttype)
			self.end_headers()
			self.wfile.write(f.read())
			f.close()
		elif self.path.startswith('/api?query='):
			query = self.path.replace('/api?query=', '')
			query = urllib.parse.unquote(query)
			print('query: ', query)
			## TODO resolve mock
			rankedList = queryexec.getRankedListMock()
			##
			contenttype = 'application/json'
			body = json.dumps(rankedList)
			self.send_response(200)
			self.send_header('Content-type',contenttype)
			self.end_headers()
			self.wfile.write(bytearray(body, 'utf-8'))
		else:
			path = './ui/dist' + self.path
			contenttype = 'application/javascript'
			print("path: ", path)
			f = f = open(path, 'rb')
			self.send_response(200)
			self.send_header('Content-type',contenttype)
			self.end_headers()
			self.wfile.write(f.read())
			f.close()
		return

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()