import json
import requests

def handler(request, response):
    if request.method != "POST":
        return response.status(405).json({"error": "Only POST allowed"})

    try:
        body = request.json()
        url = body.get("url")
        data = body.get("data")

        if not url or not data:
            return response.status(400).json({"error": "Missing fields"})

        r = requests.post(url, json=data)
        return response.status(r.status_code).json({"text": r.text})
    except Exception as e:
        return response.status(500).json({"error": str(e)})
