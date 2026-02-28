from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import json
HOST = "localhost"
PORT = 8000
ROUTES = {
    ("GET", "/users"): "get_users",
    ("PUT", "/users"): "update_user",
    ("DELETE", "/users"): "delete_user",
}
# Simulated database
USERS = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"},
]
class SimpleAPI(BaseHTTPRequestHandler):
    # Common JSON response helper
    def send_json(self, status=200, data=None):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        if data is not None:
            self.wfile.write(json.dumps(data).encode())
    # Extract query parameters
    def get_params(self):
        parsed = urlparse(self.path)
        return parse_qs(parsed.query)
    # Extract request body (for PUT)
    def read_body(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length)
        return json.loads(body) if body else {}
    # Central router
    def handle_route(self):
        parsed = urlparse(self.path)
        route = (self.command, parsed.path)
        handler_name = ROUTES.get(route)
        if not handler_name:
            self.send_json(404, {"error": "Route not found"})
            return
        handler = getattr(self, handler_name)
        handler()
    # HTTP method handlers
    def do_GET(self): self.handle_route()
    def do_PUT(self): self.handle_route()
    def do_DELETE(self): self.handle_route()
    # ---------- CONTROLLERS ----------
    # GET /users
    def get_users(self):
        self.send_json(200, {"data": USERS})
    # PUT /users?id=3
    def update_user(self):
        params = self.get_params()
        user_id = params.get("id", [None])[0]
        if not user_id:
            self.send_json(400, {"error": "id is required"})
            return
        user_id = int(user_id)
        body = self.read_body()
        for user in USERS:
            if user["id"] == user_id:
                user.update(body)
                self.send_json(200, {"message": "User updated", "user": user})
                return
        self.send_json(404, {"error": "User not found"})
    # DELETE /users?id=3
    def delete_user(self):
        params = self.get_params()
        user_id = params.get("id", [None])[0]
        if not user_id:
            self.send_json(400, {"error": "id is required"})
            return
        user_id = int(user_id)
        for user in USERS:
            if user["id"] == user_id:
                USERS.remove(user)
                self.send_json(200, {"message": "User deleted", "deleted": user})
                return
        self.send_json(404, {"error": "User not found"})
def run():
    server = HTTPServer((HOST, PORT), SimpleAPI)
    print(f"Server running on http://{HOST}:{PORT}")
    server.serve_forever()
if __name__ == "__main__":
    run()
