
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

RESEMBLE_API_KEY = "RBMY3xzlld3nyJaWr8FaSwtt"
RESEMBLE_VOICE_UUID = "f4641ad8"

@app.route('/synthesize_audio', methods=['POST'])
def synthesize_audio():
    data = request.get_json()
    text = data.get('text')

    if not text:
        return jsonify({"error": "No text provided"}), 400

    headers = {
        "Authorization": f"Token {RESEMBLE_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "voice_uuid": RESEMBLE_VOICE_UUID,
        "text": text
    }

    response = requests.post("https://app.resemble.ai/api/v2/clips", headers=headers, json=payload)

    if response.status_code == 200:
        audio_url = response.json().get("audio_url")
        return jsonify({"audio_url": audio_url}), 200
    else:
        return jsonify({"error": "Failed to generate audio"}), 500

if __name__ == '__main__':
    app.run()
