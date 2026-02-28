from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import json
import time

HOST = "localhost"
PORT = 8000

NOTES = {}        # id → {"id": 1, "text": "..."}
NEXT_ID = 1

RATE_LIMIT = {}   # ip → [timestamps]
MAX_REQUESTS = 5
WINDOW = 60       # 60 seconds window

API_KEY = "mykey123"

shutdown_requested = False


# ------------------------------------------------------
# Helper: Rate Limit Checker
# ------------------------------------------------------
def rate_limited(ip):
    now = time.time()
    RATE_LIMIT.setdefault(ip, [])

    # Remove old hits
    RATE_LIMIT[ip] = [t for t in RATE_LIMIT[ip] if now - t < WINDOW]

    if len(RATE_LIMIT[ip]) >= MAX_REQUESTS:
        return True

    RATE_LIMIT[ip].append(now)
    return False


# ------------------------------------------------------
# Main API Handler
# ------------------------------------------------------
class API(BaseHTTPRequestHandler):

    # ---------------- JSON Response Helper -----------------
    def send_json(self, status, data=None):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        if data is not None:
            self.wfile.write(json.dumps(data).encode())

    def send_no_content(self):
        self.send_response(204)
        self.end_headers()

    def read_json(self):
        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length)
        if not raw:
            return None
        try:
            return json.loads(raw)
        except:
            return None

    # ------------------------------------------------------
    # DO NOT override .handle() — instead use .process_request()
    # ------------------------------------------------------
    def process_request(self):
        global shutdown_requested, NEXT_ID

        ip = self.client_address[0]

        # ------------- Task 9: Rate Limiting -----------------
        if rate_limited(ip):
            self.send_json(429, {"error": "Too Many Requests"})
            return

        # ------------- Parse Request -------------------------
        parsed = urlparse(self.path)
        path = parsed.path
        parts = path.strip("/").split("/")

        # =====================================================
        # Task 1 — Health Check
        # =====================================================
        if self.command == "GET" and path == "/health":
            self.send_json(200, {"status": "ok"})
            return

        # =====================================================
        # Task 2 / 3 / 4 / 5 / 6 / 7 — Notes API
        # =====================================================
        if parts[0] == "notes":

            # ------------------ GET /notes (list + search) ----
            if self.command == "GET" and len(parts) == 1:
                qs = parse_qs(parsed.query)
                search = qs.get("search", [None])[0]

                notes_list = list(NOTES.values())

                # Task 7: Search
                if search:
                    s = search.lower()
                    notes_list = [n for n in notes_list if s in n["text"].lower()]

                self.send_json(200, notes_list)
                return

            # ------------------ POST /notes (create) ----------
            if self.command == "POST" and len(parts) == 1:
                body = self.read_json()
                if not body or "text" not in body:
                    self.send_json(400, {"error": "Missing text"})
                    return

                note = {"id": NEXT_ID, "text": body["text"]}
                NOTES[NEXT_ID] = note
                NEXT_ID += 1

                self.send_json(201, note)
                return

            # ------------- All /notes/{id} variants ------------
            if len(parts) == 2:
                # Extract ID safely
                try:
                    note_id = int(parts[1])
                except:
                    self.send_json(400, {"error": "Invalid ID"})
                    return

                # ---------------- GET /notes/{id} --------------
                if self.command == "GET":
                    if note_id not in NOTES:
                        self.send_json(404, {"error": "Note not found"})
                        return
                    self.send_json(200, NOTES[note_id])
                    return

                # ---------------- PUT /notes/{id} --------------
                if self.command == "PUT":
                    if note_id not in NOTES:
                        self.send_json(404, {"error": "Note not found"})
                        return

                    body = self.read_json()
                    if not body or "text" not in body:
                        self.send_json(400, {"error": "Invalid JSON"})
                        return

                    NOTES[note_id]["text"] = body["text"]
                    self.send_json(200, NOTES[note_id])
                    return

                # ---------------- DELETE /notes/{id} -----------
                if self.command == "DELETE":
                    if note_id not in NOTES:
                        self.send_json(404, {"error": "Note not found"})
                        return

                    del NOTES[note_id]
                    self.send_no_content()
                    return

        # =====================================================
        # Task 8 — API Key Auth
        # =====================================================
        if path == "/secret":
            key = self.headers.get("X-API-Key")

            if key != API_KEY:
                self.send_json(401, {"error": "Unauthorized"})
                return

            self.send_json(200, {"secret": "Access granted"})
            return

        # =====================================================
        # Task 10 — Graceful Shutdown
        # =====================================================
        if path == "/shutdown" and self.command == "POST":
            if self.client_address[0] != "127.0.0.1":
                self.send_json(403, {"error": "Forbidden"})
                return

            self.send_json(200, {"message": "Shutting down..."})
            shutdown_requested = True
            return

        # ------------- Default 404 ---------------------------
        self.send_json(404, {"error": "Not Found"})


    # ---------------- HTTP METHOD BINDINGS ------------------
    def do_GET(self): self.process_request()
    def do_POST(self): self.process_request()
    def do_PUT(self): self.process_request()
    def do_DELETE(self): self.process_request()


# ------------------------------------------------------
# Run + Graceful Shutdown Loop
# ------------------------------------------------------
def run():
    global shutdown_requested
    server = HTTPServer((HOST, PORT), API)

    print(f"Server running at http://{HOST}:{PORT}")

    # Manually handle each request so we can shut down gracefully
    while not shutdown_requested:
        server.handle_request()

    print("Server shutting down...")


if __name__ == "__main__":
    run()
