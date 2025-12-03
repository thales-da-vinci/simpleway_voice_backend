import os, uuid, sys
from flask import Flask, request, jsonify, send_file
from coqui_tts import speak_text
from vosk_stt import recognize_speech

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "SimpleWay Voice Engine ativo 🕯️",
        "python_version": sys.version
    })

@app.route('/speak', methods=['POST'])
def tts_route():
    try:
        data = request.get_json(force=True)
        text = data.get('text', '')
        lang = data.get('lang', 'en')
        filename = f"static/output/{uuid.uuid4()}.wav"
        speak_text(text, filename, lang)
        return send_file(filename, mimetype="audio/wav")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/listen', methods=['POST'])
def stt_route():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "Nenhum arquivo enviado"}), 400
        audio_file = request.files['file']
        lang = request.form.get('lang', 'en')
        transcript = recognize_speech(audio_file, lang)
        return jsonify({"transcript": transcript})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    os.makedirs("static/output", exist_ok=True)
    app.run(host='0.0.0.0', port=5000)
