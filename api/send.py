import json
import requests

def handler(request):
    try:
        print("👉 Yeni istek geldi")  # 🟢 LOG 1

        if request.method != "POST":
            print("❌ GET isteği geldi, reddedildi")  # 🟢 LOG 2
            return {
                "statusCode": 405,
                "body": json.dumps({"error": "Only POST allowed"})
            }

        body_raw = request.body.decode()
        print(f"📦 Ham veri:\n{body_raw}")  # 🟢 LOG 3

        data = json.loads(body_raw)
        url = data.get("url")
        payload = data.get("data")

        if not url or not payload:
            print("❗ Eksik alanlar")  # 🟢 LOG 4
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing 'url' or 'data'"})
            }

        print(f"📤 Webhook gönderiliyor:\nURL: {url}\nPayload: {payload}")  # 🟢 LOG 5

        r = requests.post(url, json=payload)
        print(f"✅ Webhook yanıtı: {r.status_code} - {r.text}")  # 🟢 LOG 6

        return {
            "statusCode": r.status_code,
            "body": r.text
        }

    except Exception as e:
        print(f"🔥 HATA: {str(e)}")  # 🟢 LOG 7
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
