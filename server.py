import json
from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
import yaml

from src.property.app import App

with open('config.yml', 'r') as file:
    configs = yaml.safe_load(file)

print(configs)

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        response = App.get_response("GET", self.path)
        self.send_response(200)
        self.wfile.write(bytes(json.dumps(response["body"], ensure_ascii=False), 'utf-8'))


if __name__ == '__main__':
    httpd = HTTPServer(('127.0.0.1', 8000), MyHandler)
    httpd.serve_forever()
