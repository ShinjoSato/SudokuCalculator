# -*- coding: utf-8 -*-
import http.server as server
import socket
import json
from src.py.main import main

class SudokuHandler(server.BaseHTTPRequestHandler):
    def do_POST(self):
        #Get a request.
        print("Get a request.")
        content_len  = int(self.headers.get("content-length"))
        body = json.loads(self.rfile.read(content_len))
        result=main(body)
        response={
            'result': result
        }
        #Response.
        self.send_response(200)
        self.send_header('Content-type', 'application/json;')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        body_json = json.dumps(response, sort_keys=False, indent=4, ensure_ascii=False) 
        self.wfile.write(body_json.encode("utf-8"))

#Start a server.
host=socket.gethostname()
#ip=socket.gethostbyname(host)
ip="127.0.0.1"
port = 3333
print("IP ADDRESS:",ip,"\nPORT:",port)
httpd = server.HTTPServer((ip, port), SudokuHandler)
httpd.serve_forever()