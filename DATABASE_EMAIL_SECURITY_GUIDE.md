# 🚀 Database, Email & Security Setup Guide

## ✅ Improvements Made (Items 1, 3, 6)

### 1️⃣ **Database Setup (SQLite + SQLAlchemy)**

#### What Changed:
- **Old**: In-memory data storage (resets on server restart)
- **New**: SQLite database with persistent data

#### Models Created:
```
✓ Admin - Admin user accounts
✓ Customer - Customer accounts with OTP
✓ Product - Laptop inventory
✓ Order - Customer orders
✓ OrderItem - Items in each order
✓ PasswordResetToken - Password reset tokens
```

#### Benefits:
- ✅ Data persists after server restart
- ✅ Query optimization
- ✅ Relationships management
- ✅ Easy to upgrade to PostgreSQL/MySQL

---

### 3️⃣ **Email & SMS Notifications**

#### Features Implemented:

**1. OTP via Email**
```
- 6-digit OTP generation
- Automatic expiry in 10 minutes
- Email sending on registration
```

**2. Order Confirmation Email**
```
- Automatic email after order placement
- Order details included
- Professional HTML template
```

**3. Password Reset Email**
```
- Reset link sent to email
- 1-hour token expiry
- Secure token generation
```

#### Setup Required:
```
1. Enable 2FA on Gmail
2. Generate App Password
3. Add to .env file:
   MAIL_USERNAME=your-email@gmail.com
   MAIL_PASSWORD=your-app-password
```

---

### 6️⃣ **Security Improvements**

#### Implemented:
✅ **Password Hashing**
- Using `bcrypt` (not plain text)
- Secure password storage
- Password validation

✅ **Environment Variables**
- Sensitive data in `.env`
- Not hardcoded in code
- Easy configuration per environment

✅ **Input Validation**
- Email format validation
- Phone number validation
- Required field checks
- SQL injection prevention

✅ **Authentication**
- Token-based auth
- Secure token generation
- Bearer token validation

✅ **Error Handling**
- Sanitized error messages
- No sensitive info in responses
- Proper HTTP status codes

---

## 📋 Installation Steps

### Step 1: Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### Step 2: Configure Email (.env file)

**For Gmail:**
1. Go to Google Account Settings
2. Enable 2-Step Verification
3. Generate App Password
4. Copy password to `.env` file

```env
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=xxxx xxxx xxxx xxxx
```

**Alternative (Test without Email):**
```env
MAIL_SERVER=localhost
MAIL_PORT=1025
```

### Step 3: Initialize Database
```bash
python server_v2.py
```

Then visit:
```
POST http://localhost:5000/api/init-db
```

Response:
```json
{
  "success": true,
  "message": "Database initialized with sample data"
}
```

---

## 🔐 Security Checklist

- [x] Passwords hashed with bcrypt
- [x] OTP expires after 10 minutes
- [x] Reset tokens expire after 1 hour
- [x] Input validation on all endpoints
- [x] CORS enabled for frontend
- [x] Token authentication on protected endpoints
- [x] Environment variables for secrets
- [x] Database relationships defined

---

## 📧 Email Templates

### 1. OTP Email
```
Subject: Your OTP for Second Hand PC Studio
Body: 6-digit code + 10 min expiry
```

### 2. Order Confirmation
```
Subject: Order Confirmation - [ORDER_NUMBER]
Body: Order details, total price, payment method
```

### 3. Password Reset
```
Subject: Password Reset - Second Hand PC Studio
Body: Reset link (expires in 1 hour)
```

---

## 🧪 Testing Endpoints

### 1. Health Check
```bash
curl http://localhost:5000/api/health
```

### 2. Register Customer
```bash
curl -X POST http://localhost:5000/api/customer/register \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test User",
    "email": "test@example.com",
    "phone": "9876543210",
    "password": "password123"
  }'
```

### 3. Verify OTP
```bash
curl -X POST http://localhost:5000/api/customer/verify-otp \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": 1,
    "otp": "123456"
  }'
```

### 4. Customer Login
```bash
curl -X POST http://localhost:5000/api/customer/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "password123"
  }'
```

### 5. Forgot Password
```bash
curl -X POST http://localhost:5000/api/customer/forgot-password \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com"
  }'
```

### 6. Create Order
```bash
curl -X POST http://localhost:5000/api/orders \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "customer_id": 1,
    "items": [
      {
        "product_id": 1,
        "quantity": 1
      }
    ],
    "payment_method": "upi",
    "shipping_address": {
      "street": "123 Main St",
      "city": "Mumbai",
      "pincode": "400001"
    }
  }'
```

---

## 🔄 Migration from Old Server

### Old Server (server.py)
- In-memory storage
- No email
- Plain text passwords
- No validation

### New Server (server_v2.py)
- SQLite database
- Email notifications
- Hashed passwords
- Full validation

### How to Switch:
1. Backup old data (if needed)
2. Rename `server.py` to `server_backup.py`
3. Rename `server_v2.py` to `server.py`
4. Restart Flask server
5. Test endpoints

---

## 📊 Database Schema

```
admins
├── id (PK)
├── username
├── email
├── phone
├── password_hash
├── bank_details
└── upi_details

customers
├── id (PK)
├── name
├── email
├── phone
├── password_hash
├── otp
├── otp_expires
├── is_verified
└── orders (FK)

products
├── id (PK)
├── brand
├── model
├── processor
├── ram
├── storage
├── condition
├── price
├── original_price
├── warranty
├── rating
├── reviews_count
├── stock
└── order_items (FK)

orders
├── id (PK)
├── order_number
├── customer_id (FK)
├── total_price
├── gst
├── final_price
├── payment_method
├── status
├── shipping_address
└── items (OrderItem FK)

order_items
├── id (PK)
├── order_id (FK)
├── product_id (FK)
├── quantity
└── price

password_reset_tokens
├── id (PK)
├── customer_id (FK)
├── token
└── expires_at
```

---

## ⚠️ Important Configuration

### Email Setup (Gmail)

1. **Generate App Password:**
   - Open Google Account Security
   - Enable 2-Step Verification
   - Generate 16-character App Password
   - Use in `.env` file

2. **Less Secure Apps (Alternative):**
   - Go to Account Security
   - Enable "Less secure app access"
   - Use Gmail password directly

### Environment Variables

```env
# Database
DATABASE_URL=sqlite:///laptop_shop.db

# Email (Gmail)
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password

# Security
SECRET_KEY=your-super-secret-key-minimum-32-chars
```

---

## 🚀 Deployment Ready

This version is ready for:
- ✅ Production deployment
- ✅ Database upgrade (PostgreSQL)
- ✅ Email integration
- ✅ Secure authentication
- ✅ Data persistence
- ✅ Error handling
- ✅ Input validation

---

## 📞 Support Endpoints

All endpoints now support:
- ✅ Input validation
- ✅ Error handling
- ✅ JSON responses
- ✅ HTTP status codes
- ✅ CORS headers
- ✅ Token authentication (protected routes)

---

## 🔄 Next Steps

1. **Update Frontend** to use new APIs
2. **Test Email** functionality
3. **Verify Database** persistence
4. **Security Audit** before production
5. **Load Testing** for scalability
