#!/usr/bin/python3

import http.server, json
data = {"name": "John", "age": 30, "city": "New York"}
jsoned_data = json.dumps(data)
info = {"version": "1.0", "description": "A simple API built with http.server"}
jsoned_info = json.dumps(info)
class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/data":
            self.send_response(200)
            self.send_header("content-type","application/json")
            self.end_headers()
            self.wfile.write(jsoned_data.encode("utf-8"))

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("content-type","application/json")
            self.end_headers()
            self.wfile.write(jsoned_info.encode("utf-8"))

        elif self.path == "/":
            self.send_response(200)
            self.send_header("content-type","text/plain")
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("content-type","text/plain")
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode("utf-8"))


        else:
            self.send_response(404)
            self.send_header("content-type","text/plain")
            self.end_headers()
            self.wfile.write("Endpoint not found".encode("utf-8"))
        

port = 8000
httpd = http.server.HTTPServer(("",port),MyHandler)
print(f"{port} is now open")
httpd.serve_forever()