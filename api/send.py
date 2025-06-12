import json
import requests

print("🔥 HANDLER YÜKLENDİ")

def handler(request):
    print("📥 İstek alındı")

    try:
        # Vercel’de request.json() önce deneyip, olmazsa body.decode ile yüklüyoruz
        try:
            data = request.json()
        except:
            data = json.loads(request.body.decode("utf-8"))

        print("📦 Body:", data)

        url = data.get("url")
        payload = data.get("data")

        if not url or not payload:
            print("⚠️ Eksik veri")
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing 'url' or 'data'"})
            }

        print("🚀 Webhook’a POST:", url)
        resp = requests.post(url, json=payload)
        print("✅ Discord’dan dönen kod:", resp.status_code)

        return {
            "statusCode": resp.status_code,
            "body": resp.text
        }

    except Exception as e:
        print("❌ GENEL HATA:", str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

handler = handler
