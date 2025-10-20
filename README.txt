# Picnic Vakti — Tek Paket (PWA + Flask + TWA)

## 1) GitHub'a yükle
git init
git add .
git commit -m "Picnic PWA ready"
git branch -M main
git remote add origin <repo-url>
git push -u origin main

## 2) Yayınla (Render)
New Web Service → Python → Procfile/tüm dosyalar bu repo
- Start command: (Procfile var) → `gunicorn server:app`

## 3) PWABuilder
URL: https://picnic-3.onrender.com
Package for Stores → Android
- Package ID: com.asen.picnic
- VersionCode: 9 (bir sonraki yüklemede +1 yap)
- Signing: Use mine (keystore/alias şifrelerinle) veya Generate new
AAB indir.

## 4) Google Play Console
- Uygulama paket adı: com.asen.picnic
- İlk kurulumda “Google’ın imzalama anahtarını yönetmesine izin ver”
- Sürüm oluştur → AAB yükle → Kaydet → Gözden geçir → Yayınla

## Kontrol
- /manifest.json, /service-worker.js → 200
- /static/icons/icon-192.png, icon-512.png → 200
- /.well-known/assetlinks.json → 200
