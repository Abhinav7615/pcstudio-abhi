# ⚡ QUICK START - 3 STEPS

## Step 1: Install Dependencies (First Time Only)
```bash
cd backend
pip install -r requirements.txt
```

## Step 2: Start Backend Server
```bash
cd backend
python server.py
```
✅ Server running on: **http://localhost:5000**

## Step 3: Open Website
- Use VS Code Live Server on **index.html**
- Or open: **http://localhost:5500**

---

## 🔐 Admin Login (NEW - Dedicated Page)

1. Open: **http://localhost:5500**
2. Click **Login** → **Admin Login** button
3. You'll be taken to `pages/admin-login.html`
4. Enter credentials:
   - Username: `admin`
   - Password: `admin123`
5. Click **Login**
6. ✅ Redirects to admin dashboard (`pages/admin.html`)

**Note**: Admin login now uses a dedicated backend-connected page for security.

---

## 📂 Important Files

| File | Purpose |
|------|---------|
| `backend/server.py` | Backend API server |
| `backend/requirements.txt` | Python dependencies |
| `pages/admin-login.html` | Admin login page (NEW) |
| `pages/admin.html` | Admin dashboard |
| `pages/checkout.html` | Checkout (Pay Now button) |
| `FULL_SETUP_GUIDE.md` | Complete documentation |

---

## 🚨 Troubleshooting

**Backend not starting?**
```bash
pip install Flask flask-cors
python server.py
```

**Port 5000 in use?**
```bash
# Windows:
netstat -ano | findstr :5000
taskkill /PID [PID] /F
```

**Frontend showing API errors?**
- Backend must be running on port 5000
- Frontend on port 5500
- Check browser F12 console

**Admin login redirects to home?**
- Ensure backend is running: `python server.py`
- Check DevTools → Storage → `adminToken` is set
- Hard reload: Ctrl+Shift+Delete then F5

---

## 💳 Customer Checkout - Pay Now (NEW)

**Pay Now** (immediate payment + order marked as paid):
1. Add items to cart → Checkout page
2. Fill all fields, select **UPI** or **Card**
3. Click **Pay Now**
4. Confirmation modal appears
5. Click **Confirm & Pay**
6. Order saved with `status: 'paid'` + transaction ID
7. Success modal + cart cleared

**Place Order** (for any method, admin confirms):
- Order saved as `status: 'pending'`
- Admin will call customer to confirm

---

**Status**: ✅ READY TO USE  
**Admin Login**: ✅ NEW PAGE  
**Admin Dashboard**: ✅ TOKEN PROTECTED  
**Payment Flow**: ✅ CONFIRMATION REQUIRED
