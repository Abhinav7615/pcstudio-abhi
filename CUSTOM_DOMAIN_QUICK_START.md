# 🌐 Custom Domain Setup - Quick Start

## **pcstudioabhi.com** Setup

---

## ⚡ **Quick 3-Step Setup (5 Minutes)**

### **Step 1: Run Domain Setup Script** 🚀

**Option A - Batch File (Easiest):**
1. Right-click: `setup-domains.bat`
2. Select: "Run as Administrator"
3. Done! ✅

**Option B - PowerShell:**
1. Right-click PowerShell
2. Select "Run as Administrator"
3. Run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
4. Run: `.\setup-domains.ps1`

---

### **Step 2: Verify Setup** ✓

```powershell
ping pcstudioabhi.com
```

**Expected Output:**
```
Pinging pcstudioabhi.com [127.0.0.1] with 32 bytes of data
```

✅ If you see `127.0.0.1`, setup is successful!

---

### **Step 3: Access Website** 🌐

**Now open in browser:**
- **Frontend:** http://pcstudioabhi.com:5500
- **Backend:** http://api.pcstudioabhi.com:5000
- **Admin Panel:** http://admin.pcstudioabhi.com:5500

---

## 📋 **What Gets Configured**

```
Your Hosts File Will Have:
├─ 127.0.0.1 pcstudioabhi.com
├─ 127.0.0.1 www.pcstudioabhi.com
├─ 127.0.0.1 admin.pcstudioabhi.com
└─ 127.0.0.1 api.pcstudioabhi.com
```

---

## ✨ **Benefits**

✅ Professional domain name  
✅ Easy to remember  
✅ Test like production  
✅ All subdomains work  
✅ Perfect for development  

---

## 🔧 **Troubleshooting**

### **Domain not resolving?**
```powershell
# Clear DNS cache
ipconfig /flushdns

# Restart in PowerShell
Clear-DnsClientCache
```

### **Error: Access Denied**
- ✓ Make sure PowerShell runs as Administrator
- ✓ Check User Account Control settings

### **Still not working?**
```powershell
# Manual hosts file edit
notepad C:\Windows\System32\drivers\etc\hosts

# Add these lines at end:
127.0.0.1 pcstudioabhi.com
127.0.0.1 www.pcstudioabhi.com
127.0.0.1 admin.pcstudioabhi.com
127.0.0.1 api.pcstudioabhi.com
```

---

## 🎯 **Frontend & Backend Configuration**

✅ **Automatically Configured!**

`js/app.js` now detects:
- **Localhost** → Uses `http://localhost:5000/api`
- **Custom Domain** → Uses `http://api.pcstudioabhi.com:5000/api`
- **Production** → Uses `https://api.pcstudioabhi.com/api`

**No manual changes needed!**

---

## 📱 **Test All Subdomains**

```bash
# Frontend
http://pcstudioabhi.com:5500

# Frontend - WWW
http://www.pcstudioabhi.com:5500

# Backend API
http://api.pcstudioabhi.com:5000

# Admin Panel
http://admin.pcstudioabhi.com:5500
```

---

## 🔐 **Security Note**

**Local Setup (Current):**
- Uses HTTP (not HTTPS)
- Safe for development only
- Perfect for testing

**When going Production:**
- Setup proper SSL/HTTPS
- Use Let's Encrypt (free)
- Register real domain
- Point DNS to server

See: `DOMAIN_SETUP_GUIDE.md` for production setup

---

## 📊 **Status Check**

```
Before Setup:
├─ Frontend: http://localhost:5500 ✓
├─ Backend: http://localhost:5000 ✓
└─ API: http://localhost:5000/api ✓

After Setup:
├─ Frontend: http://pcstudioabhi.com:5500 ✓
├─ Backend: http://api.pcstudioabhi.com:5000 ✓
├─ Admin: http://admin.pcstudioabhi.com:5500 ✓
└─ API: http://api.pcstudioabhi.com:5000/api ✓
```

---

## 🎉 **All Done!**

Your website is now running on custom domain:

```
🌐 pcstudioabhi.com
```

**Next Steps:**
1. ✓ Setup complete
2. Access website with custom domain
3. Test all features
4. Ready for production deployment!

---

## 📞 **Support**

**Issues?**
1. Clear DNS cache: `ipconfig /flushdns`
2. Restart browser
3. Clear browser cache (Ctrl+Shift+Delete)
4. Check if servers are running (ports 5000, 5500)

**Backup Hosts File:**
- Created: `C:\Windows\System32\drivers\etc\hosts.backup`
- Can restore if needed

---

**Enjoy your custom domain! 🚀**
