import json
import requests

def handler(request):
    try:
        if request.method != "POST":
            return {
                "statusCode": 405,
                "body": json.dumps({"error": "Only POST allowed"})
            }

        body = request.body.decode()
        payload = json.loads(body)

        url = payload.get("url")
        data = payload.get("data")

        if not url or not data:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing 'url' or 'data'"})
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
