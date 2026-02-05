from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import json
messages = []
class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers['Content-Length'])
        data = self.rfile.read(length)
        msg = json.loads(data)
        messages.append(msg)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"ok")
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps(messages).encode())
class ThreadedServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True
server = ThreadedServer(('localhost', 8000), Handler)
print("Chat server running on http://localhost:8000")
server.serve_forever()
