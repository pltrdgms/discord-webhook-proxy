import json
import requests
from http.server import BaseHTTPRequestHandler

def handler(request):
    try:
        if request.method != "POST":
            return Response(405, {"error": "Only POST allowed"})

        body = request.body.decode("utf-8")
        data = json.loads(body)

        url = data.get("url")
        payload = data.get("data")

        if not url or not payload:
            return Response(400, {"error": "Missing 'url' or 'data'"})

        r = requests.post(url, json=payload)
        return Response(r.status_code, r.text)
    
    except Exception as e:
        return Response(500, {"error": str(e)})


class Response:
    def __init__(self, status_code, body):
        self.status_code = status_code
        self.body = json.dumps(body) if isinstance(body, dict) else body
        self.headers = {"Content-Type": "application/json"}


handler = handler
