from gtts import gTTS

def speak_text(text, filename, lang='en'):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save(filename)
