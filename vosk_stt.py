import vosk, json, soundfile as sf, os

def recognize_speech(audio_file, lang='en'):
    model_path = f"models/vosk-model-small-{lang}-us-0.15" if lang == "en" else "models/vosk-model-small-pt-br-0.3"
    if not os.path.exists(model_path):
        return {"error": f"Modelo Vosk {lang} não encontrado"}
    model = vosk.Model(model_path)
    audio_data, samplerate = sf.read(audio_file)
    rec = vosk.KaldiRecognizer(model, samplerate)
    rec.AcceptWaveform(audio_data.tobytes())
    return json.loads(rec.Result()).get("text", "")
