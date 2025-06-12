import json
import requests



url = "https://discord.com/api/webhooks/1352987309305233408/WqpZEWcT4x766fGa1Jr0J2KlZX0fbvQdsjxmiziCTCK4ThiJ1I7z2_WfCvXOywUgJJoE" # webhook url, from here: https://i.imgur.com/f9XnAew.png

# for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
data = {
    "content" : "message content",
    "username" : "custom username"
}

# leave this out if you dont want an embed
# for all params, see https://discordapp.com/developers/docs/resources/channel#embed-object
data["embeds"] = [
    {
        "description" : "text in embed",
        "title" : "embed title"
    }
]






def handler(request):
    result = requests.post(url, json = data)

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print(f"Payload delivered successfully, code {result.status_code}.")
    try:
        if request.method != "POST":
            return {
                "statusCode": 405,
                "body": json.dumps({"error": "Only POST allowed"})
            }

        body = request.body.decode()
        data = json.loads(body)

        url = data.get("url")
        payload = data.get("data")

        if not url or not payload:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing 'url' or 'data'"})
            }

        r = requests.post(url, json=payload)

        return {
            "statusCode": r.status_code,
            "body": r.text
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
