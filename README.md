# SimpleWay Voice Backend 🎙️

API Flask com suporte a:
- TTS (Text-to-Speech) via Coqui TTS
- STT (Speech-to-Text) via Vosk

## Rotas

### POST /speak
Gera áudio a partir de texto.
```bash
curl -X POST -H "Content-Type: application/json" -d '{"text": "Hello, SimpleWay!", "lang": "en"}' https://simpleway-voice.onrender.com/speak --output voice.wav
```

### POST /listen
Transcreve áudio enviado.
```bash
curl -X POST -F "file=@sample.wav" -F "lang=en" https://simpleway-voice.onrender.com/listen
```

## Deploy

Deploy gratuito via [Render.com](https://render.com)

1. Conecte este repositório no Render
2. Configure:
   - Environment: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - Instance Type: Free Tier

## Estrutura

```
simpleway_voice_backend/
├── app.py              # Servidor Flask
├── coqui_tts.py       # TTS engine
├── vosk_stt.py        # STT engine
├── requirements.txt   # Dependências
├── static/output/     # Arquivos de áudio gerados
└── models/            # Modelos Vosk
```

## v6.3.1 - The Eternal Voice 🕯️
