# 🚀 Second Hand PC Studio - Complete Setup Guide

## ✅ What's Been Fixed

### ✨ Admin Login Backend Integration
- ❌ **BEFORE**: "Admin login - Backend integration needed"
- ✅ **AFTER**: Full working admin authentication with backend API

### 📦 Backend System Created
- Python Flask REST API server
- Admin login/authentication endpoints
- Customer login & registration
- Product management APIs
- Order tracking system
- Dashboard statistics

---

## 🎯 Quick Start (5 Minutes)

### Step 1: Install Python Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### Step 2: Start Backend Server
```bash
python server.py
```

✅ **Expected Output:**
```
✅ Backend Server is running on http://localhost:5000
🔐 Admin credentials: username: admin, password: admin123
📊 API endpoints available at http://localhost:5000/api
```

### Step 3: Start Frontend (in separate terminal/tab)
```bash
# Option A: Use VS Code Live Server extension
# Right-click on index.html → Open with Live Server
# (Opens on http://localhost:5500)

# Option B: Use Python's built-in server
cd path/to/project
python -m http.server 5500
```

### Step 4: Test Admin Login
1. Open browser: `http://localhost:5500`
2. Click "Login" button
3. Select "Admin Login" tab
4. Enter credentials:
   - Username: `admin`
   - Password: `admin123`
5. Click "Login" button
6. ✅ You should be redirected to admin dashboard!

---

## 🔐 Default Credentials

### Admin Account
```
Username: admin
Password: admin123
Email: admin@secondhandpcstudio.com
```

---

## 📁 Project Structure

```
Second Hand PC Studio/
├── index.html                      # Main website
├── backend/
│   ├── server.py                  # Flask backend server ⭐
│   └── requirements.txt           # Python dependencies
├── js/
│   └── app.js                     # Frontend + API integration ⭐
├── css/
│   ├── style.css
│   └── responsive.css
├── pages/
│   ├── admin.html                 # Admin dashboard
│   └── [other pages...]
├── BACKEND_SETUP.md               # Backend documentation
├── DOMAIN_SETUP.md                # Domain configuration
└── start-backend.bat              # Quick start script (Windows)
```

---

## 🌐 What's New

### Backend Features (server.py)
- ✅ Admin Login API
- ✅ Customer Registration API
- ✅ Customer Login API
- ✅ Product Management (CRUD)
- ✅ Order Management
- ✅ Dashboard Statistics
- ✅ Change Password API
- ✅ CORS enabled for frontend communication

### Frontend Updates (js/app.js)
- ✅ Removed all "Backend integration needed" alerts
- ✅ Real API calls to backend
- ✅ Token-based authentication
- ✅ Error handling & validation
- ✅ Session management with localStorage

---

## 🔌 API Endpoints Ready

### Authentication
- `POST /api/admin/login` - Admin login
- `POST /api/customer/login` - Customer login
- `POST /api/customer/register` - Customer registration
- `POST /api/admin/change-password` - Change password

### Dashboard & Data
- `GET /api/admin/stats` - Dashboard statistics
- `GET /api/admin/orders` - Get all orders
- `GET /api/admin/products` - Get all products
- `GET /api/admin/customers` - Get all customers

### Product Management
- `POST /api/admin/products` - Add product
- `PUT /api/admin/products/:id` - Update product
- `DELETE /api/admin/products/:id` - Delete product

---

## 🌐 Website URL Setup

### Local Development (Current)
- **Frontend**: http://localhost:5500
- **Backend API**: http://localhost:5000/api

### Production Setup
To change to your custom domain (e.g., secondhandpcstudio.com):

1. **Edit [js/app.js](js/app.js)** - Line 1:
```javascript
// Change:
const API_URL = 'http://localhost:5000/api';

// To your domain:
const API_URL = 'https://secondhandpcstudio.com/api';
```

2. See [DOMAIN_SETUP.md](DOMAIN_SETUP.md) for detailed domain configuration

---

## 🛠️ Troubleshooting

### ❌ "Python not found"
- Install Python from [python.org](https://www.python.org)
- Add Python to PATH during installation

### ❌ "Port 5000 already in use"
```bash
# Windows: Find process using port 5000
netstat -ano | findstr :5000

# Kill the process or use different port:
# Edit server.py, change: app.run(debug=True, port=5001)
```

### ❌ "Module not found: flask"
```bash
pip install Flask flask-cors
```

### ❌ "CORS errors in browser console"
- Make sure backend is running on port 5000
- Frontend running on port 5500
- CORS is already enabled in server.py

### ❌ "Admin login still shows alert"
- Clear browser cache (Ctrl+Shift+Delete)
- Make sure backend server is running
- Check browser console for errors (F12)

---

## 📝 Next Steps

### To Complete Setup:
1. ✅ Install Python dependencies
2. ✅ Start backend server
3. ✅ Start frontend on different port
4. ✅ Test admin login

### To Customize:
- [ ] Change admin password in [backend/server.py](backend/server.py)
- [ ] Update website name/branding
- [ ] Connect real database (MySQL/MongoDB)
- [ ] Implement email verification
- [ ] Add payment gateway
- [ ] Deploy to production

### For Production:
- [ ] Switch to production database
- [ ] Setup environment variables
- [ ] Enable HTTPS
- [ ] Setup proper authentication (JWT)
- [ ] Add input validation & security
- [ ] Deploy to hosting service

---

## 📚 Documentation Files

- [BACKEND_SETUP.md](BACKEND_SETUP.md) - Detailed backend guide
- [DOMAIN_SETUP.md](DOMAIN_SETUP.md) - Domain & URL configuration
- [README.md](README.md) - Project overview

---

## 🎉 You're All Set!

Your e-commerce website with admin authentication is now **fully functional**!

**Start the servers and test it out!** 🚀

Questions? Check the documentation files or review the source code.

---

**Created**: February 2, 2026  
**Status**: ✅ Backend Integration Complete
