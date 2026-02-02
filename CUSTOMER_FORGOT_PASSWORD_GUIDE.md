# Customer Forgot Password Feature - Complete Guide

## Overview
A complete forgot password system has been added for customers with security hints showing password patterns.

## What's New ✨

### 1. **Customer Forgot Password Modal** 
   - New tab in the customer login modal
   - Accessible via "Forgot Password?" link in login form
   - Two-step reset process:
     1. **Step 1**: Enter email → Receive 6-digit reset code + password hint
     2. **Step 2**: Enter code + new password → Reset complete

### 2. **Password Hint Display**
   - Shows hint like: `A*****3` (first & last char visible)
   - Helps customers verify their account
   - Displayed in blue information box

### 3. **Backend Endpoints**

#### POST `/api/customer/forgot-password`
- **Purpose**: Generate reset code and send to email
- **Request**:
  ```json
  {
    "email": "customer@example.com"
  }
  ```
- **Response**:
  ```json
  {
    "success": true,
    "message": "Reset code sent to email@example.com",
    "resetCode": "123456",
    "passwordHint": "Password hint: A*****3"
  }
  ```
- **Error Cases**:
  - Email not found: 404
  - Missing email: 400

#### POST `/api/customer/reset-password`
- **Purpose**: Verify code and reset password
- **Request**:
  ```json
  {
    "email": "customer@example.com",
    "resetCode": "123456",
    "newPassword": "newPassword123"
  }
  ```
- **Response**:
  ```json
  {
    "success": true,
    "message": "Password reset successfully"
  }
  ```
- **Validations**:
  - Code must match (3 attempts max)
  - Password minimum 6 characters
  - All fields required
  - Reset token expires after failed attempts

## Frontend Implementation

### Updated Files

#### `index.html`
- Added "Forgot Password?" link under password field in login form
- New forgot password tab with two steps:
  - Step 1: Email input + "Send Reset Code" button
  - Step 2: Reset code + new password + confirm password inputs
  - Password hint display box
- Form IDs added for proper data binding

#### `js/app.js`
- **Function**: `requestCustomerPasswordReset()`
  - Validates email input
  - Calls `/api/customer/forgot-password`
  - Shows reset code in demo
  - Displays password hint
  - Toggles to step 2

- **Function**: `resetCustomerPassword()`
  - Validates all inputs
  - Checks password match
  - Calls `/api/customer/reset-password`
  - Shows success/error messages
  - Redirects to login after success

### Form Input IDs
```html
<!-- Login Form -->
<input id="loginEmail" type="email">
<input id="loginPassword" type="password">

<!-- Register Form -->
<input id="registerName" type="text">
<input id="registerEmail" type="email">
<input id="registerPhone" type="tel">
<input id="registerPassword" type="password">

<!-- Forgot Password Form -->
<input id="forgotEmail" type="email">
<input id="resetCode" type="text">
<input id="newPassword" type="password">
<input id="confirmPassword" type="password">
```

## Usage Flow

### For Customer
1. Click "Login" in navigation
2. In login modal, click "Forgot Password?" link
3. Enter registered email
4. Click "Send Reset Code"
5. Receive 6-digit code + password hint (shown in demo)
6. Enter code + new password + confirm
7. Click "Reset Password"
8. Success message displays
9. Auto-redirects to login after 2 seconds
10. Login with new password

## Backend Features

### Security Features
- **Attempt Limiting**: Max 3 failed attempts per reset request
- **Token Expiration**: Reset token deleted after successful reset
- **Password Validation**: Minimum 6 characters required
- **Data Storage**: Reset tokens stored in memory with timestamp

### Data Structure
```python
password_reset_tokens = {
    "email@example.com": {
        "code": "123456",
        "timestamp": "2024-01-01T10:30:00",
        "attempts": 0,
        "userType": "customer"
    }
}
```

## Testing Guide

### Test Case 1: Valid Password Reset
```
Email: existing@email.com
Reset Code: [code from response]
New Password: TestPass123
Expected: Success message, redirect to login
```

### Test Case 2: Invalid Code
```
Email: existing@email.com
Reset Code: 999999
Expected: "Invalid reset code" error (max 3 attempts)
```

### Test Case 3: Password Mismatch
```
New Password: TestPass123
Confirm Password: DifferentPass456
Expected: "Passwords do not match" error
```

### Test Case 4: Email Not Found
```
Email: nonexistent@email.com
Expected: "Email not found in system" error (404)
```

## API Structure Comparison

### Admin Forgot Password (Already Exists)
- Endpoint: `/api/admin/forgot-password`
- Endpoint: `/api/admin/reset-password`
- Page: `pages/admin-login.html`

### Customer Forgot Password (NEW)
- Endpoint: `/api/customer/forgot-password`
- Endpoint: `/api/customer/reset-password`
- Page: `index.html` (auth modal)

## Status Messages & Colors

| Status | Color | Example |
|--------|-------|---------|
| Success | Green (#16a34a) | "✅ Success! Password reset successfully" |
| Error | Red (#dc2626) | "❌ Error message" |
| Info | Blue (#2563eb) | "Demo: Reset code: 123456" |
| Hint | Blue (#1e40af) | "Password hint: A*****3" |

## Next Steps (Optional Enhancements)

1. **Email Integration**
   - Replace demo code display with actual email sending
   - Use SMTP or email service (SendGrid, AWS SES)

2. **Security Questions**
   - Add security questions during registration
   - Verify questions before showing password hint
   - Alternative to email verification

3. **Token Expiration**
   - Add time-based expiration (e.g., 15 minutes)
   - Show timer on UI

4. **Database Integration**
   - Replace in-memory storage with database
   - Add customer password history
   - Log password reset attempts

5. **Two-Factor Authentication**
   - Add SMS verification after email
   - Use authenticator app

## File Changes Summary

### Modified Files
1. **backend/server.py**
   - Added `/api/customer/forgot-password` endpoint
   - Added `/api/customer/reset-password` endpoint
   - Added `password_reset_tokens` dictionary

2. **index.html**
   - Added "Forgot Password?" link in login form
   - Added forgot password tab with 2-step UI
   - Added form input IDs for JavaScript binding

3. **js/app.js**
   - Added `requestCustomerPasswordReset()` function
   - Added `resetCustomerPassword()` function

## Troubleshooting

### Issue: "Failed to fetch" on password reset
**Solution**: Ensure backend is running on localhost:5000
```bash
cd backend
python server.py
```

### Issue: Form not submitting
**Solution**: Check that all required inputs have proper IDs (loginEmail, loginPassword, etc.)

### Issue: Password hint not displaying
**Solution**: Verify password hint is returned in API response and that passwordHintDisplay div is not hidden

### Issue: Automatic redirect not working
**Solution**: Check browser console for JavaScript errors, ensure `switchAuthTab('login')` function exists

## Demo Credentials

To test customer forgot password:

1. First, register a new customer:
   - Email: `test@example.com`
   - Password: `TestPass123`

2. Then test forgot password:
   - Email: `test@example.com`
   - You'll get a 6-digit code shown in blue box
   - Enter code + new password to reset

## Support

For issues or questions:
- Check backend console for errors
- Check browser console (F12) for JavaScript errors
- Verify API endpoints are working in Postman
- Check CORS settings in Flask if experiencing network issues

---

**Version**: 1.0  
**Date**: 2024  
**Status**: ✅ Complete & Ready to Use
