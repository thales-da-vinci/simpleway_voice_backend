from TTS.api import TTS

def speak_text(text, filename, lang='en'):
    model = "tts_models/en/ljspeech/tacotron2-DDC" if lang == "en" else "tts_models/pt/cv/vits"
    tts = TTS(model_name=model, progress_bar=False, gpu=False)
    tts.tts_to_file(text=text, file_path=filename)
