# ⚡ QUICK REFERENCE - Customer Forgot Password

## 🚀 How to Use (Customer)

### Way 1: Using Forgot Password Tab (NEW!)
```
1. Click "Login" → "Forgot Password?" link
2. Enter email → "Send Reset Code"
3. Copy 6-digit code (shown in blue box - DEMO)
4. Enter code + new password
5. Click "Reset Password" → ✅ Done!
```

### Way 2: Direct Steps
- **URL**: http://127.0.0.1:5500 (Live Server)
- **Login Modal**: Press "Login" button
- **Tab**: Click "Forgot Password?" link
- **Enter Email**: Your registered email
- **Get Code**: Appears in blue box (DEMO)
- **New Password**: Min 6 characters
- **Confirm**: Must match
- **Submit**: Click "Reset Password"

## 🔧 Backend Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/customer/forgot-password` | POST | Get reset code |
| `/api/customer/reset-password` | POST | Set new password |

## 📝 Request/Response Examples

### Request 1: Get Reset Code
```json
POST /api/customer/forgot-password
{
  "email": "john@example.com"
}

Response:
{
  "success": true,
  "resetCode": "123456",
  "passwordHint": "J**n"
}
```

### Request 2: Reset Password
```json
POST /api/customer/reset-password
{
  "email": "john@example.com",
  "resetCode": "123456",
  "newPassword": "NewPass123"
}

Response:
{
  "success": true,
  "message": "Password reset successfully"
}
```

## ✅ Validation Rules

- Email must be registered
- Reset code must be 6 digits
- Password minimum 6 characters
- Passwords must match
- Max 3 wrong attempts

## 🎯 Status Messages

| Message | Color | Meaning |
|---------|-------|---------|
| ✅ Password reset successfully | Green | Done! |
| ❌ Invalid reset code | Red | Wrong code |
| ❌ Passwords do not match | Red | Confirm again |
| ❌ Email not found | Red | Not registered |
| Demo: Reset code: XXXXXX | Blue | Code for testing |
| Password hint: X****Y | Blue | Account verification |

## 📍 Files Changed

```
backend/server.py
├── Added: /api/customer/forgot-password
├── Added: /api/customer/reset-password
└── Data: password_reset_tokens

index.html
├── Added: "Forgot Password?" link
├── Added: forgot-password tab
├── Added: Form input IDs
└── Structure: 2-step UI

js/app.js
├── Added: requestCustomerPasswordReset()
├── Added: resetCustomerPassword()
├── Features: Validation, API calls, UI updates
└── Timing: Auto-redirect after success
```

## 🐛 Quick Troubleshooting

| Issue | Fix |
|-------|-----|
| "Failed to fetch" | Start backend: `python server.py` |
| Code not showing | Check API response in browser console |
| Form not working | Check form input IDs match |
| Auto-redirect fails | Check JavaScript console for errors |
| Email error | Make sure email is registered first |

## 🧪 Test Case

```bash
1. Register: test@example.com / Test123
2. Logout
3. Click "Forgot Password?"
4. Enter: test@example.com
5. Get code: 123456 (shown in box)
6. Enter code: 123456
7. New password: NewTest456
8. Confirm: NewTest456
9. Reset → Success!
10. Login with: test@example.com / NewTest456
```

## 📌 Demo vs Real

| Feature | Demo | Real |
|---------|------|------|
| Reset Code | Blue box | Email |
| Password Hint | Blue box | Email + Blue box |
| Speed | Instant | ~2-3 seconds |
| Storage | Memory | Database |
| Email | No | Yes |

## 🔐 Security Features

✅ Attempt Limiting (max 3 tries)  
✅ Code Validation  
✅ Password Requirements  
✅ Token Expiration  
✅ Hint Display  

## 📱 UI Flow

```
┌─────────────┐
│Login Modal  │
└──────┬──────┘
       │ Click "Forgot Password?"
       ↓
┌──────────────────────┐
│Forgot Password Tab   │
│Step 1: Get Code      │
│[Email Input]         │
│[Send Code Button]    │
└──────────────────────┘
       │ Click "Send Code"
       ↓
┌──────────────────────┐
│Step 2: Reset Pass    │
│[Code Input]          │
│[Password Input]      │
│[Confirm Input]       │
│[Reset Button]        │
└──────────────────────┘
       │ Click "Reset"
       ↓
┌──────────────────────┐
│✅ Success Message    │
│Auto-redirect login   │
└──────────────────────┘
```

## 🎓 Use Case Example

**John forgot his password:**
1. Opens website
2. Clicks "Login" → "Forgot Password?" 
3. Enters: john@example.com
4. Gets code: 654321
5. Enters code + new password: JohnNew123
6. Success! Can login now

**Admin forgot password:**
- Different: pages/admin-login.html
- Similar: 2-step process with email code
- Reference: ADMIN_FORGOT_PASSWORD_GUIDE.md

## 📞 Support

- Backend Issues: Check `python server.py` running
- Frontend Issues: Check browser F12 console
- API Issues: Test with Postman
- CORS Issues: Backend CORS is enabled ✅

---

**Quick Start**: 
1. Start backend: `cd backend && python server.py`
2. Open: http://127.0.0.1:5500
3. Click "Login" → "Forgot Password?"
4. Follow 2-step process
5. ✅ Done!
