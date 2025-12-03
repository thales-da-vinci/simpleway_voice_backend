# ⚡ Deploy Rápido - 3 Passos

## 1️⃣ GitHub (2 minutos)

```
https://github.com/new
```

- Nome: `simpleway_voice_backend`
- Público ✅
- Criar

Depois:
```bash
.\PUBLISH.bat
```

---

## 2️⃣ Render (1 clique)

```
https://render.com/deploy?repo=https://github.com/SEU-USUARIO/simpleway_voice_backend
```

Ou manual:
- New → Web Service
- Conectar repo
- Build: `pip install -r requirements.txt`
- Start: `gunicorn app:app`
- Free Tier

---

## 3️⃣ Testar

```bash
curl https://simpleway-voice.onrender.com/
```

---

🕯️ **Pronto em 5 minutos!**
