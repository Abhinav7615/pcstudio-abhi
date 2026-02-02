# Code Changes - Customer Forgot Password Implementation

## Overview
This document shows the exact code changes made to implement customer forgot password feature.

---

## File 1: backend/server.py

### Location: After the existing get_customers() endpoint (around line 140)

### Code Added:
```python
# Customer Forgot Password - Get Hint
@app.route('/api/customer/forgot-password', methods=['POST'])
def customer_forgot_password():
    data = request.get_json()
    email = data.get('email')
    
    if not email:
        return jsonify({'success': False, 'message': 'Email is required'}), 400
    
    customer = next((c for c in customers if c['email'] == email), None)
    
    if not customer:
        return jsonify({'success': False, 'message': 'Email not found in system'}), 404
    
    # Generate reset code
    import random
    import string
    reset_code = ''.join(random.choices(string.digits, k=6))
    
    # Get password hint (first 3 chars + asterisks)
    password = customer.get('password', '')
    hint = password[0] + '*' * (len(password) - 2) + password[-1] if len(password) > 2 else '***'
    
    if email not in password_reset_tokens:
        password_reset_tokens[email] = {}
    
    password_reset_tokens[email] = {
        'code': reset_code,
        'timestamp': datetime.now().isoformat(),
        'attempts': 0,
        'userType': 'customer'
    }
    
    return jsonify({
        'success': True, 
        'message': f'Reset code sent to {email}',
        'resetCode': reset_code,  # Demo purposes
        'passwordHint': f'Password hint: {hint}'
    }), 200

# Customer Reset Password
@app.route('/api/customer/reset-password', methods=['POST'])
def customer_reset_password():
    data = request.get_json()
    email = data.get('email')
    reset_code = data.get('resetCode')
    new_password = data.get('newPassword')
    
    if not email or not reset_code or not new_password:
        return jsonify({'success': False, 'message': 'All fields are required'}), 400
    
    if email not in password_reset_tokens:
        return jsonify({'success': False, 'message': 'Password reset request not found. Request again.'}), 404
    
    token_data = password_reset_tokens[email]
    
    if token_data.get('userType') != 'customer':
        return jsonify({'success': False, 'message': 'Invalid reset token'}), 401
    
    if token_data['code'] != reset_code:
        token_data['attempts'] += 1
        if token_data['attempts'] >= 3:
            del password_reset_tokens[email]
            return jsonify({'success': False, 'message': 'Too many failed attempts. Request password reset again.'}), 403
        return jsonify({'success': False, 'message': 'Invalid reset code'}), 401
    
    customer = next((c for c in customers if c['email'] == email), None)
    
    if not customer:
        return jsonify({'success': False, 'message': 'Customer not found'}), 404
    
    if len(new_password) < 6:
        return jsonify({'success': False, 'message': 'Password must be at least 6 characters'}), 400
    
    customer['password'] = new_password
    del password_reset_tokens[email]
    
    return jsonify({'success': True, 'message': 'Password reset successfully'}), 200
```

---

## File 2: index.html

### Change 1: Updated Customer Login Form (Line ~170-179)

**Before**:
```html
<div id="loginTab" class="auth-tab-content active">
    <h3>Customer Login</h3>
    <form id="customerLoginForm" onsubmit="handleCustomerLogin(event)">
        <input type="email" placeholder="Email" required class="form-input">
        <input type="password" placeholder="Password" required class="form-input">
        <button type="submit" class="btn btn-primary btn-block">Login</button>
        <p class="or-divider">OR</p>
        <button type="button" class="btn btn-secondary btn-block" onclick="switchAuthTab('otp')">Login with OTP</button>
    </form>
</div>
```

**After**:
```html
<div id="loginTab" class="auth-tab-content active">
    <h3>Customer Login</h3>
    <form id="customerLoginForm" onsubmit="handleCustomerLogin(event)">
        <input type="email" id="loginEmail" placeholder="Email" required class="form-input">
        <input type="password" id="loginPassword" placeholder="Password" required class="form-input">
        <button type="submit" class="btn btn-primary btn-block">Login</button>
        <p style="text-align:center; margin-top:10px;">
            <a href="#" onclick="switchAuthTab('forgot-password'); return false;" style="color:#2563eb; text-decoration:none; font-size:14px;">Forgot Password?</a>
        </p>
        <p class="or-divider">OR</p>
        <button type="button" class="btn btn-secondary btn-block" onclick="switchAuthTab('otp')">Login with OTP</button>
    </form>
</div>
```

### Change 2: Added Forgot Password Tab (Insert before OTP Tab, ~Line 210)

```html
<!-- Customer Forgot Password -->
<div id="forgot-passwordTab" class="auth-tab-content">
    <h3>Reset Password</h3>
    <div id="forgotPasswordStep1">
        <p style="color: #666; margin-bottom: 20px; font-size: 14px;">Enter your email to receive a password reset code</p>
        <input type="email" id="forgotEmail" placeholder="Enter your email" required class="form-input">
        <button type="button" class="btn btn-primary btn-block" onclick="requestCustomerPasswordReset()">Send Reset Code</button>
        <p style="text-align:center; margin-top:15px;">
            <a href="#" onclick="switchAuthTab('login'); return false;" style="color:#2563eb; text-decoration:none; font-size:14px;">Back to Login</a>
        </p>
    </div>
    <div id="forgotPasswordStep2" style="display:none;">
        <p style="color: #666; margin-bottom: 15px; font-size: 14px;">Enter the code sent to your email</p>
        <div id="passwordHintDisplay" style="background: #f0f9ff; padding: 12px; border-radius: 5px; margin-bottom: 15px; border-left: 4px solid #2563eb; display: none;">
            <p style="margin: 0; font-size: 13px; color: #1e40af;"><strong>Password Hint:</strong> <span id="passwordHintText"></span></p>
        </div>
        <input type="text" id="resetCode" placeholder="6-digit code" maxlength="6" required class="form-input">
        <input type="password" id="newPassword" placeholder="New Password (min 6 chars)" required class="form-input">
        <input type="password" id="confirmPassword" placeholder="Confirm Password" required class="form-input">
        <button type="button" class="btn btn-primary btn-block" onclick="resetCustomerPassword()">Reset Password</button>
        <p style="text-align:center; margin-top:15px;">
            <a href="#" onclick="switchAuthTab('login'); return false;" style="color:#2563eb; text-decoration:none; font-size:14px;">Back to Login</a>
        </p>
    </div>
    <div id="forgotPasswordStatus"></div>
</div>
```

### Change 3: Updated Register Form with IDs (Line ~180-195)

**Before**:
```html
<form id="customerRegisterForm" onsubmit="handleCustomerRegister(event)">
    <input type="text" placeholder="Full Name" required class="form-input">
    <input type="email" placeholder="Email" required class="form-input">
    <input type="tel" placeholder="Phone Number" required class="form-input">
    <input type="password" placeholder="Password (min 6 chars)" required class="form-input">
    <input type="password" placeholder="Confirm Password" required class="form-input">
```

**After**:
```html
<form id="customerRegisterForm" onsubmit="handleCustomerRegister(event)">
    <input type="text" id="registerName" placeholder="Full Name" required class="form-input">
    <input type="email" id="registerEmail" placeholder="Email" required class="form-input">
    <input type="tel" id="registerPhone" placeholder="Phone Number" required class="form-input">
    <input type="password" id="registerPassword" placeholder="Password (min 6 chars)" required class="form-input">
    <input type="password" placeholder="Confirm Password" required class="form-input">
```

---

## File 3: js/app.js

### Location: After the sendOtpAdmin() function (around line 620)

### Code Added:

```javascript
// Customer Forgot Password Functions
async function requestCustomerPasswordReset() {
    const email = document.getElementById('forgotEmail').value;
    const statusDiv = document.getElementById('forgotPasswordStatus');
    
    if (!email) {
        statusDiv.innerHTML = '<p style="color: #dc2626; font-size: 14px;">Please enter your email</p>';
        return;
    }

    try {
        const response = await fetch(`${API_URL}/customer/forgot-password`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email })
        });

        const data = await response.json();

        if (data.success) {
            // Show step 2
            document.getElementById('forgotPasswordStep1').style.display = 'none';
            document.getElementById('forgotPasswordStep2').style.display = 'block';
            
            // Display password hint
            if (data.passwordHint) {
                document.getElementById('passwordHintDisplay').style.display = 'block';
                document.getElementById('passwordHintText').textContent = data.passwordHint.replace('Password hint: ', '');
            }
            
            // Demo: Show reset code in status
            statusDiv.innerHTML = `<p style="color: #2563eb; font-size: 13px; background: #f0f9ff; padding: 10px; border-radius: 5px; border-left: 4px solid #2563eb;"><strong>Demo:</strong> Reset code: <strong>${data.resetCode}</strong></p>`;
        } else {
            statusDiv.innerHTML = `<p style="color: #dc2626; font-size: 14px;">${data.message}</p>`;
        }
    } catch (error) {
        statusDiv.innerHTML = `<p style="color: #dc2626; font-size: 14px;">Error: ${error.message}</p>`;
    }
}

async function resetCustomerPassword() {
    const email = document.getElementById('forgotEmail').value;
    const resetCode = document.getElementById('resetCode').value;
    const newPassword = document.getElementById('newPassword').value;
    const confirmPassword = document.getElementById('confirmPassword').value;
    const statusDiv = document.getElementById('forgotPasswordStatus');
    
    if (!email || !resetCode || !newPassword || !confirmPassword) {
        statusDiv.innerHTML = '<p style="color: #dc2626; font-size: 14px;">All fields are required</p>';
        return;
    }
    
    if (newPassword.length < 6) {
        statusDiv.innerHTML = '<p style="color: #dc2626; font-size: 14px;">Password must be at least 6 characters</p>';
        return;
    }
    
    if (newPassword !== confirmPassword) {
        statusDiv.innerHTML = '<p style="color: #dc2626; font-size: 14px;">Passwords do not match</p>';
        return;
    }

    try {
        const response = await fetch(`${API_URL}/customer/reset-password`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 
                email, 
                resetCode, 
                newPassword 
            })
        });

        const data = await response.json();

        if (data.success) {
            statusDiv.innerHTML = `<p style="color: #16a34a; font-size: 14px; background: #f0fdf4; padding: 10px; border-radius: 5px; border-left: 4px solid #16a34a;"><strong>✅ Success!</strong> ${data.message}</p>`;
            
            // Reset form and go back to login after 2 seconds
            setTimeout(() => {
                document.getElementById('forgotPasswordStep1').style.display = 'block';
                document.getElementById('forgotPasswordStep2').style.display = 'none';
                document.getElementById('forgotEmail').value = '';
                document.getElementById('resetCode').value = '';
                document.getElementById('newPassword').value = '';
                document.getElementById('confirmPassword').value = '';
                statusDiv.innerHTML = '';
                switchAuthTab('login');
            }, 2000);
        } else {
            statusDiv.innerHTML = `<p style="color: #dc2626; font-size: 14px;">${data.message}</p>`;
        }
    } catch (error) {
        statusDiv.innerHTML = `<p style="color: #dc2626; font-size: 14px;">Error: ${error.message}</p>`;
    }
}
```

---

## Summary of Changes

### backend/server.py
- **Lines Added**: ~60
- **Functions Added**: 2 (`customer_forgot_password`, `customer_reset_password`)
- **New Features**: Password hint generation, attempt limiting, token management

### index.html
- **Lines Added**: ~35
- **Form Elements Added**: 5 inputs + 2 divs
- **New Tab**: forgot-password tab with 2-step UI
- **Added Links**: "Forgot Password?" and "Back to Login"
- **Added IDs**: forgotEmail, resetCode, newPassword, confirmPassword, loginEmail, loginPassword, registerName, registerEmail, registerPhone, registerPassword

### js/app.js
- **Lines Added**: ~85
- **Functions Added**: 2 (`requestCustomerPasswordReset`, `resetCustomerPassword`)
- **Features**: Email validation, API calls, UI toggles, error handling, success redirect

---

## Testing the Changes

### Test Endpoint 1 (Get Reset Code):
```bash
curl -X POST http://localhost:5000/api/customer/forgot-password \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com"}'
```

### Test Endpoint 2 (Reset Password):
```bash
curl -X POST http://localhost:5000/api/customer/reset-password \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","resetCode":"123456","newPassword":"NewPass123"}'
```

---

## Verification Checklist

- [x] Backend endpoints added
- [x] Frontend UI created
- [x] JavaScript functions implemented
- [x] Form inputs have proper IDs
- [x] Error handling included
- [x] Password validation added
- [x] Attempt limiting implemented
- [x] Password hints display correctly
- [x] Auto-redirect on success
- [x] Status messages styled
- [x] All files saved

---

**Status**: ✅ All changes implemented and verified
