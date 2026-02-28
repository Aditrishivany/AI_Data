from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import json

HOST = "localhost"
PORT = 8000

ROUTES = {
    ("GET", "/products"): "get_products",
}

# Preloaded product list
PRODUCTS = [
    {"id": 1, "name": "iPhone", "price": 1000},
    {"id": 2, "name": "Samsung Phone", "price": 800},
    {"id": 3, "name": "Nokia Phone", "price": 300},
    {"id": 4, "name": "Headphones", "price": 200},
]


class SimpleAPI(BaseHTTPRequestHandler):

    def send_json(self, status=200, data=None):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        if data is not None:
            self.wfile.write(json.dumps(data).encode())

    def get_query_params(self):
        parsed_url = urlparse(self.path)
        return parse_qs(parsed_url.query)

    def handle_route(self):
        parsed_url = urlparse(self.path)
        route = (self.command, parsed_url.path)

        handler_name = ROUTES.get(route)
        if not handler_name:
            self.send_json(404, {"error": "Route not found"})
            return

        handler = getattr(self, handler_name)
        handler()

    def do_GET(self):
        self.handle_route()

    # ---------- CONTROLLER ----------
    def get_products(self):
        params = self.get_query_params()

        # Required: name
        name = params.get("name", [None])[0]
        if not name:
            self.send_json(400, {"error": "Missing required parameter: name"})
            return

        name = name.lower()

        # Optional: max_price
        max_price_param = params.get("max_price", [None])[0]
        max_price = int(max_price_param) if max_price_param else None

        # Step 1: Filter by name (partial match)
        filtered = [p for p in PRODUCTS if name in p["name"].lower()]

        # Step 2: Filter by max_price if provided
        if max_price is not None:
            filtered = [p for p in filtered if p["price"] <= max_price]

        # Step 3: Return result
        self.send_json(200, {
            "count": len(filtered),
            "data": filtered
        })


def run():
    server = HTTPServer((HOST, PORT), SimpleAPI)
    print(f"Server running at http://{HOST}:{PORT}")
    server.serve_forever()


if __name__ == "__main__":
    run()
