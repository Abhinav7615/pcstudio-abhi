# ⚡ **LIVE DEPLOYMENT - 30 MINUTES**

## 🎯 **DO THIS NOW:**

---

### **📍 STEP 1: Git (5 min)**

```powershell
cd c:\Users\ASUS\OneDrive\Desktop\Laptop
git init
git add .
git commit -m "Initial commit"
```

---

### **📍 STEP 2: GitHub (3 min)**

1. Go: https://github.com/new
2. Name: `pcstudio-abhi`
3. Create
4. Copy commands shown

---

### **📍 STEP 3: Push (5 min)**

```bash
git remote add origin https://github.com/YOUR_USERNAME/pcstudio-abhi.git
git branch -M main
git push -u origin main
```

---

### **📍 STEP 4: Render Backend (10 min)**

1. Go: https://render.com
2. Sign up with GitHub
3. New Web Service
4. Select repository
5. Settings:
   ```
   Build: pip install -r requirements.txt
   Start: gunicorn server_v2:app
   ```
6. Environment Variables:
   ```
   MAIL_USERNAME=your-email
   MAIL_PASSWORD=your-password
   SECRET_KEY=random-key
   ```
7. Deploy!

**Your backend URL:**
```
https://pcstudio-abhi-backend.onrender.com
```

---

### **📍 STEP 5: Vercel Frontend (5 min)**

1. Go: https://vercel.com
2. Sign up with GitHub
3. Import Project
4. Select repository
5. Deploy!

**Your frontend URL:**
```
https://pcstudio-abhi.vercel.app
```

---

### **📍 STEP 6: Test (2 min)**

Open browser:
```
https://pcstudio-abhi.vercel.app
```

✅ Should show your website!

---

## 🎉 **DONE! WEBSITE IS LIVE!**

```
🌐 https://pcstudio-abhi.vercel.app
```

---

## ⏱️ **Total Time: 30 Minutes**

Go! Do it now! 🚀
