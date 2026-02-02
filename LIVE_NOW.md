# ⚡ **ABHI KAR DENE WALA GUIDE** 

## 🎯 **Bas 15 Minutes Mein Live!**

---

## 1️⃣ **Git Download & Install** (2 min)

```
https://git-scm.com/download/windows
Install → Next Next → Done → Restart PowerShell
```

---

## 2️⃣ **GitHub Account** (2 min)

```
https://github.com/signup
Create account → Verify email
```

---

## 3️⃣ **GitHub Repository** (2 min)

```
https://github.com/new
Name: pcstudio-abhi → Create
```

---

## 4️⃣ **Push Code to GitHub** (3 min)

```powershell
cd c:\Users\ASUS\OneDrive\Desktop\Laptop
git init
git add .
git commit -m "PCStudio Abhi"

git remote add origin https://github.com/YOUR_USERNAME/pcstudio-abhi.git
git branch -M main
git push -u origin main
```

---

## 5️⃣ **Deploy Backend (Render)** (5 min)

```
https://render.com/register
→ Sign with GitHub
→ Dashboard → New Web Service
→ Select repository
→ Build: pip install -r requirements.txt
→ Start: gunicorn server_v2:app
→ Add env vars (MAIL_USERNAME, MAIL_PASSWORD, SECRET_KEY)
→ Deploy!
```

**Your URL:**
```
https://pcstudio-abhi-backend.onrender.com
```

---

## 6️⃣ **Deploy Frontend (Vercel)** (3 min)

```
https://vercel.com/signup
→ Sign with GitHub
→ New Project
→ Select repository
→ Deploy!
```

**Your URL:**
```
https://pcstudio-abhi.vercel.app
```

---

## 🎉 **KHATAM!**

```
YOUR WEBSITE IS LIVE:
https://pcstudio-abhi.vercel.app
```

**Cost: FREE**

---

**Detailed guide: [`FREE_LIVE_DEPLOYMENT.md`](FREE_LIVE_DEPLOYMENT.md)**
