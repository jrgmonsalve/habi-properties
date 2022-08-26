#!/usr/bin/env python
import os
from http.server import HTTPServer
from http.server import SimpleHTTPRequestHandler
import yaml

with open('settings.yml', 'r') as file:
    settings = yaml.safe_load(file)

print(settings['user'][0])

ROUTES = [
    ('/', '/var/www/doc-html')
]

class MyHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # default root -> cwd        
        root = os.getcwd()
        
        # look up routes and get root directory
        for patt, rootDir in ROUTES:
            if path.startswith(patt):                
                path = path[len(patt):]
                root = rootDir
                break
        # new path
        return os.path.join(root, path)    

if __name__ == '__main__':
    httpd = HTTPServer(('127.0.0.1', 8000), MyHandler)
    httpd.serve_forever()