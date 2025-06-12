import json
import requests

def handler(request):
    if request.method != "POST":
        return {
            "statusCode": 405,
            "body": json.dumps({"error": "Only POST allowed"})
        }

    try:
        body = request.json()
        url = body.get("url")
        data = body.get("data")

        if not url or not data:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing fields"})
            }

        r = requests.post(url, json=data)
        return {
            "statusCode": r.status_code,
            "body": r.text
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
