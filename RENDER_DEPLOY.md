# 🚀 Deploy no Render.com

## Passo a Passo

### 1. Criar Repositório no GitHub

```bash
# Criar repo no GitHub: simpleway_voice_backend
# Depois:
git remote add origin https://github.com/SEU-USUARIO/simpleway_voice_backend.git
git branch -M main
git push -u origin main
```

### 2. Deploy no Render

1. Acesse [https://render.com](https://render.com)
2. Clique em **New → Web Service**
3. Conecte o repositório `simpleway_voice_backend`
4. Configure:
   - **Name:** simpleway-voice
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Instance Type:** Free

5. Clique em **Create Web Service**

### 3. Aguardar Deploy

O Render levará ~5-10 minutos para:
- Instalar dependências
- Baixar modelos TTS
- Iniciar servidor

### 4. Obter URL

Após deploy, a URL será:
```
https://simpleway-voice.onrender.com
```

### 5. Testar

```bash
curl https://simpleway-voice.onrender.com/
```

Resposta esperada:
```json
{"status": "SimpleWay Voice Engine ativo 🕯️"}
```

---

## ⚠️ Importante

### Modelos Vosk

Os modelos Vosk NÃO estão no repositório (são grandes).

**Opções:**

1. **Usar apenas TTS** (sem STT por enquanto)
2. **Baixar modelos no build** (adicionar script)
3. **Usar serviço STT externo** (Google/AWS)

### Free Tier Render

- ✅ Gratuito
- ⚠️ Dorme após 15 min de inatividade
- ⚠️ Primeira requisição pode demorar ~30s (cold start)

---

## 🔄 Atualizar App Flutter

Edite `lib/services/audio_service.dart`:

```dart
final String baseUrl = "https://simpleway-voice.onrender.com";
```

---

🕯️ **Sistema pronto para deploy gratuito!**
