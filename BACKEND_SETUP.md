# Backend Setup Guide

## 📋 Prerequisites
- Python 3.7+ - [Download](https://www.python.org/downloads/)
- pip (comes with Python)

## 🚀 Quick Start

### Step 1: Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### Step 2: Start the Backend Server
```bash
python server.py
```

The server will start on **http://localhost:5000**

✅ You should see:
```
✅ Backend Server is running on http://localhost:5000
🔐 Admin credentials: username: admin, password: admin123
📊 API endpoints available at http://localhost:5000/api
```

### Step 3: Open the Website
Open `index.html` in your browser (using Live Server on port 5500)

## 📊 Default Admin Credentials
- **Username**: `admin`
- **Password**: `admin123`

## 🔌 API Endpoints

### Admin Authentication
- **POST** `/api/admin/login` - Login with username and password
- **POST** `/api/admin/change-password` - Change admin password

### Customer Authentication  
- **POST** `/api/customer/login` - Customer login
- **POST** `/api/customer/register` - Customer registration

### Admin Dashboard (Dashboard)
- **GET** `/api/admin/stats` - Get dashboard statistics
- **GET** `/api/admin/orders` - Get all orders
- **GET** `/api/admin/products` - Get all products
- **GET** `/api/admin/customers` - Get all customers

### Product Management
- **POST** `/api/admin/products` - Add new product
- **PUT** `/api/admin/products/:id` - Update product
- **DELETE** `/api/admin/products/:id` - Delete product

### Health Check
- **GET** `/api/health` - Check if server is running

## 💡 How to Test Admin Login (NEW FLOW)

1. Start the backend server: `python server.py`
2. Open website: http://localhost:5500
3. Click "Login" button
4. Click "Admin Login" (navigates to `pages/admin-login.html`)
5. Enter credentials:
   - Username: `admin`
   - Password: `admin123`
6. Click "Login"
7. You will be redirected to the Admin Dashboard (`pages/admin.html`)

**Behind the scenes:**
- `pages/admin-login.html` calls `POST /api/admin/login`
- Backend returns token + admin data
- Frontend stores in `localStorage` (`adminToken`, `admin`)
- Session flags set in `sessionStorage`
- Dashboard page checks for token on load

## 🔧 Development Mode (with auto-reload)

To automatically restart server on file changes:

```bash
pip install watchdog
python -m watchdog.auto_reload server.py
```

Or simply run with Flask debug mode (already enabled in server.py)

## 📝 Notes

- Data is stored in-memory (resets when server restarts)
- For production: Replace in-memory storage with MongoDB, PostgreSQL, or MySQL
- Add JWT tokens for secure authentication
- Implement proper password hashing with bcryptjs
- Add rate limiting and input validation

## 🐛 Troubleshooting

**Port 5000 already in use?**
```bash
# Windows: Find and kill process
netstat -ano | findstr :5000
taskkill /PID [PID_NUMBER] /F
```

**CORS errors?**
- Ensure frontend is running on port 5500
- Backend on port 5000
- CORS is already enabled in `server.py`

**Admin login page shows blank or errors?**
- Check browser F12 console for JS errors
- Verify `API_URL` in `pages/admin-login.html`
- Test backend: `curl http://localhost:5000/api/health`

**API not responding?**
```bash
# Test the server is running:
curl http://localhost:5000/api/health
```

---

## 💳 Payment & Order Status (NEW)

**Order Status:**
- `pending` — Customer placed order (awaiting admin)
- `paid` — Customer used Pay Now (payment processed)
- `processing` — Admin confirmed
- `completed` — Delivered

**Admin updates status in Dashboard → Orders**

## 🔒 Security Notes

- Tokens in `localStorage`, session flags in `sessionStorage`
- Logout clears both
- For production: use HTTP-only cookies instead
- Add rate limiting to `/api/admin/login`
- Hash passwords (bcryptjs)
- Implement refresh tokens

---

**Questions?** Check the API documentation or review `server.py` code.
