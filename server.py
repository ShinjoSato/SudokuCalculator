# -*- coding: utf-8 -*-
import http.server as server
import json
from src.main import main

class SudokuHandler(server.BaseHTTPRequestHandler):
    def do_POST(self):
        # リクエスト取得
        print("Get a request.")
        content_len  = int(self.headers.get("content-length"))
        body = json.loads(self.rfile.read(content_len))
        result=main(body)
        response={
            'result': result
        }
        #Response
        self.send_response(200)
        self.send_header('Content-type', 'application/json;')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        body_json = json.dumps(response, sort_keys=False, indent=4, ensure_ascii=False) 
        self.wfile.write(body_json.encode("utf-8"))


# サーバ起動
host = '192.168.0.5'
port = 3333
httpd = server.HTTPServer((host, port), SudokuHandler)
httpd.serve_forever()