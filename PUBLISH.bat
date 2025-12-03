@echo off
echo 🚀 Publicando Backend no GitHub...
echo.

set /p username="Digite seu usuário GitHub: "

git remote add origin https://github.com/%username%/simpleway_voice_backend.git
git branch -M main
git push -u origin main

echo.
echo ✅ Backend publicado!
echo.
echo 📋 Próximo passo: Deploy no Render
echo 1. Acesse: https://render.com
echo 2. New → Web Service
echo 3. Conecte: simpleway_voice_backend
echo 4. Build: pip install -r requirements.txt
echo 5. Start: gunicorn app:app
echo.
pause
