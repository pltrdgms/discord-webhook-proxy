import json
import requests

print("🔥 HANDLER ÇALIŞTI")  # Bu satır logda görünüyorsa çalışıyor

def handler(request):
    print("📥 İstek alındı")

    try:
        body = request.body.decode("utf-8")
        data = json.loads(body)
        print("🔎 Body:", data)

        url = data.get("url")
        payload = data.get("data")

        if not url or not payload:
            print("⚠️ Eksik veri")
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing 'url' or 'data'"})
            }

        print("📤 Webhook gönderiliyor:", url)
        response = requests.post(url, json=payload)
        print("✅ Webhook cevabı:", response.status_code)

        return {
            "statusCode": response.status_code,
            "body": response.text
        }

    except Exception as e:
        print("💥 HATA:", str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

handler = handler
