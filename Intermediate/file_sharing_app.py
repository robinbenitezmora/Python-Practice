import http.server
import socketserver
import socket
import webbrowser
import pyqrcode

from pyqrcode import QRCode

import png
import os

PORT = 8010

os.environ['USERPROFILE']

desktop = os.path.join(os.environ['USERPROFILE'], 'Desktop')

os.chdir(desktop)

Handler = http.server.SimpleHTTPRequestHandler

hostname = socket.gethostname()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8.', 80))

IP = 'http://' + s.getsockname()[0] + ':' + str(PORT)

link = IP

url = pyqrcode.create(link)

url.svg('myqr.svg', scale = 8)

webbrowser.open('myqr.svg')

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    print("serving at IP", IP)
    print("serving at link", link)
    httpd.serve_forever()
    