import json
import requests

def handler(request):
    print("✨ Handler tetiklendi!")  # Log basıncı
    try:
        if request.method != "POST":
            return {"statusCode": 405, "body": json.dumps({"error":"Only POST allowed"})}

        body = request.body.decode("utf-8")
        data = json.loads(body)
        print("Body:", data)

        url = data.get("url")
        payload = data.get("data")
        r = requests.post(url, json=payload)
        print("Discord yanıt:", r.status_code, r.text)

        return {"statusCode": r.status_code, "body": r.text}

    except Exception as e:
        print("Hata yakalandı:", e)
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
