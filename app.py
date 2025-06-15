from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

RESEMBLE_API_KEY = "RBM9Y3x1ld3ny3aW8FaSWt"
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

    return jsonify(response.json()), response.status_code
