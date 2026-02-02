# Customer Forgot Password - हिंदी गाइड (Hindi Guide)

## नई सुविधा ✨

### Customer के लिए Forgot Password
- **क्या है**: अगर कोई customer अपना password भूल जाए तो नया password reset कर सकते हैं
- **कैसे काम करता है**: Email address से verification करके 6-digit code से नया password सेट कर सकते हैं
- **फायदा**: Password hint दिखाई देगी (जैसे: A*****3) जिससे पता चल जाएगा कि यह सही account है

## स्टेप-by-स्टेप प्रक्रिया

### Customer के लिए Password Reset करना:

**Step 1 - Login Page खोलना**
1. Website पर जाओ
2. "Login" बटन दबाओ
3. Login modal खुल जाएगा

**Step 2 - Forgot Password को ढूंढना**
1. Login form में अपना email enter करो
2. Password field के नीचे "Forgot Password?" link देखो
3. इस link को क्लिक करो

**Step 3 - Reset Code लेना**
1. Forgot Password tab खुल जाएगा
2. अपना registered email enter करो
3. "Send Reset Code" बटन दबाओ
4. Email के बाद Reset Code आएगा (Blue box में दिखेगा demo में)
5. Password hint भी दिखेगी (जैसे: `A*****3` - पहला और आखिरी letter दिखेगा)

**Step 4 - नया Password Set करना**
1. 6-digit code को copy करो
2. Reset code field में paste करो
3. नया password enter करो (कम से कम 6 characters)
4. Confirm password field में फिर से same password enter करो
5. "Reset Password" बटन दबाओ
6. Success message आएगा
7. 2 seconds में automatically login page खुल जाएगा
8. अब नए password से login कर सकते हो

## कमांड्स (Commands)

### Backend Start करने के लिए:
```bash
cd backend
python server.py
```

### Testing करने के लिए:

**1. पहले नया Customer Register करो:**
- Email: test123@example.com
- Password: MyPass123

**2. फिर Forgot Password test करो:**
- Login modal खोलो
- "Forgot Password?" पर क्लिक करो
- test123@example.com enter करो
- Reset code मिलेगा (blue box में दिखेगा)
- Code enter करके नया password डालो

## Backend API (Technical)

### API 1: Password Reset Code लेने के लिए
```
POST http://localhost:5000/api/customer/forgot-password

भेजो (Send):
{
  "email": "customer@example.com"
}

मिलेगा (Get):
{
  "success": true,
  "resetCode": "123456",
  "passwordHint": "A*****3"
}
```

### API 2: नया Password Set करने के लिए
```
POST http://localhost:5000/api/customer/reset-password

भेजो (Send):
{
  "email": "customer@example.com",
  "resetCode": "123456",
  "newPassword": "NewPass123"
}

मिलेगा (Get):
{
  "success": true,
  "message": "Password reset successfully"
}
```

## Error Messages और Solutions

| Problem | Solution |
|---------|----------|
| "Failed to fetch" | Backend को चालू करो: `python server.py` |
| "Email not found" | पहले register करके account बनाओ |
| "Invalid reset code" | Code सही से enter करो (max 3 बार try कर सकते हो) |
| "Passwords do not match" | Confirm password सही से match करो |
| "Password must be at least 6 characters" | कम से कम 6 letters का password बनाओ |

## Features के साथ क्या दिखेगा

### 1. Login Form में
```
Customer Login
Email: [enter email]
Password: [enter password]
Login Button
👉 Forgot Password? (यह नया है)
```

### 2. Forgot Password Tab में
**पहला Step (Email लेना):**
```
Reset Password

Enter your email to receive a password reset code

Email: [enter email]
Send Reset Code Button

Back to Login Link
```

**दूसरा Step (Code से Password Set करना):**
```
Reset Password

Enter the code sent to your email

🔵 Password Hint: A*****3 (hint दिखेगी यहाँ)

Reset Code: [enter 6 digits]
New Password: [enter password]
Confirm Password: [confirm password]
Reset Password Button

Back to Login Link
```

## Security Features

✅ **3 बार की कोशिश**: अगर 3 बार wrong code enter करो तो फिर से email verify करना पड़ेगा

✅ **Password Minimum 6 Characters**: कम से कम 6 letters का password होना चाहिए

✅ **Password Hint**: पहला और आखिरी character दिखेगा ताकि पता चल जाए सही account है

✅ **Token Expiration**: Reset के बाद token delete हो जाता है

## Important Notes 📝

1. **Demo में** - Reset code blue box में दिखेगा
2. **Real Website में** - Reset code email पर भेजा जाएगा
3. **Backend चलाना जरूरी है** - बिना backend के काम नहीं करेगा
4. **localhost:5000** - Backend इसी port पर चलना चाहिए

## Files जो Update हुई हैं

| File | क्या बदला |
|------|----------|
| backend/server.py | 2 नई API endpoints add की |
| index.html | Forgot Password link और tab add किया |
| js/app.js | 2 नए functions add किए |

## Example: Complete Customer Forgot Password Flow

```
1. Customer Login page खोलता है
   ↓
2. "Forgot Password?" पर क्लिक करता है
   ↓
3. Email enter करता है: john@example.com
   ↓
4. "Send Reset Code" दबाता है
   ↓
5. API से reset code मिलता है: 123456
   ↓
6. Password hint दिखाई देती है: J**3
   ↓
7. 6-digit code enter करता है
   ↓
8. नया password enter करता है: NewPass789
   ↓
9. Confirm करता है
   ↓
10. "Reset Password" दबाता है
   ↓
11. ✅ Success message
   ↓
12. Automatically login page पर आ जाता है
```

## Tested Scenarios ✅

✓ Email नहीं मिलने पर error दिखाता है
✓ Wrong code enter करने पर error दिखाता है
✓ Passwords match न करने पर error दिखाता है
✓ Successfully password reset हो सकते हैं
✓ नए password से login हो सकते हैं

## Next Steps (भविष्य के लिए)

- Email integration (असली email भेजने के लिए)
- Security questions add करना
- SMS verification add करना
- Database में password history रखना

---

**Status**: ✅ तैयार है - Use कर सकते हो
**Version**: 1.0
**Language**: Hindi + English (Hinglish)
