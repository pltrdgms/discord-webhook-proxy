import json
import requests
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def _send(self, status_code, body, content_type="application/json"):
        self.send_response(status_code)
        self.send_header("Content-Type", content_type)
        self.end_headers()
        self.wfile.write(body.encode() if isinstance(body, str) else body)

    def do_POST(self):
        try:
            # Gönderilen JSON’u oku
            length = int(self.headers.get("content-length", 0))
            raw = self.rfile.read(length).decode("utf-8")
            data = json.loads(raw)

            url = data.get("url")
            payload = data.get("data")
            if not url or not payload:
                return self._send(400, json.dumps({"error": "Missing 'url' or 'data'"}))

            # Discord’a ilet
            resp = requests.post(url, json=payload)

            # Discord cevabını aynen dön
            return self._send(resp.status_code, resp.text, "text/plain")

        except Exception as e:
            return self._send(500, json.dumps({"error": str(e)}))
