from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
from urllib.parse import urlparse, parse_qs
import json
HOST = "localhost"
PORT = 8000
# This will STORE all POSTed data
DATA_STORE = []
class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True
class SimpleAPI(BaseHTTPRequestHandler):
    def _send_response(self, status, data):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path
        if path != "/echo":
            self._send_response(404, {"error": "Not found"})
            return
        content_length = int(self.headers.get("Content-Length", 0))
        raw_body = self.rfile.read(content_length)
        if not raw_body:
            self._send_response(400, {"error": "Empty body"})
            return
        try:
            body = json.loads(raw_body)
        except json.JSONDecodeError:
            self._send_response(400, {"error": "Invalid JSON"})
            return
        # STORE POST DATA
        DATA_STORE.append(body)
        self._send_response(201, {
            "message": "Data stored successfully",
            "stored_data": body,
            "total_records": len(DATA_STORE)
        })
    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        if path != "/echo":
            self._send_response(404, {"error": "Not found"})
            return
        # RETURN ALL STORED POST DATA
        self._send_response(200, {
            "message": "Fetched stored data",
            "count": len(DATA_STORE),
            "data": DATA_STORE
        })
def run():
    server = ThreadedHTTPServer((HOST, PORT), SimpleAPI)
    print(f" Server running at http://{HOST}:{PORT}")
    server.serve_forever()
if __name__ == "__main__":
    run()