# 🌐 Custom Domain Setup Guide - PCStudioAbhi

## 📋 Overview

This guide will help you set up a custom domain `pcstudioabhi.com` for your e-commerce website.

---

## 🔧 **Option 1: Local Development (Testing)**

### Step 1: Edit Windows Hosts File

**Windows Path:**
```
C:\Windows\System32\drivers\etc\hosts
```

**Steps:**
1. Open Notepad as Administrator (right-click → Run as Administrator)
2. Open file: `C:\Windows\System32\drivers\etc\hosts`
3. Add these lines at the end:

```
127.0.0.1   pcstudioabhi.com
127.0.0.1   www.pcstudioabhi.com
127.0.0.1   admin.pcstudioabhi.com
127.0.0.1   api.pcstudioabhi.com
```

4. Save file (Ctrl+S)
5. Close Notepad

**Verify:**
```powershell
ping pcstudioabhi.com
```

Expected output:
```
Pinging pcstudioabhi.com [127.0.0.1]...
```

---

### Step 2: Access Website with Custom Domain

**Frontend:**
```
http://pcstudioabhi.com:5500
```

**API/Backend:**
```
http://api.pcstudioabhi.com:5000
```

✅ **Now your website is accessible via custom domain locally!**

---

## 🌍 **Option 2: Real Domain Setup (Production)**

### Step 1: Buy Domain

**Recommended Registrars (India):**
- **Namecheap** - $8.88/year
- **GoDaddy** - ₹300-500/year
- **Hostinger** - ₹99/year (promo)
- **BigRock** - ₹199/year
- **Local** - Domain.in, Znamii.com

**Search:** `pcstudioabhi.com` on any registrar

---

### Step 2: Update DNS Records

**Add these DNS records:**

| Type | Name | Value |
|------|------|-------|
| A | @ | Your Server IP |
| A | www | Your Server IP |
| A | api | Your Server IP |
| CNAME | www | pcstudioabhi.com |

**Your Server IP:**
- Get from AWS/Heroku/DigitalOcean after deployment

---

### Step 3: Configure Backend

Update `backend/.env`:

```env
ALLOWED_HOSTS=pcstudioabhi.com,www.pcstudioabhi.com,api.pcstudioabhi.com
API_URL=https://api.pcstudioabhi.com
FRONTEND_URL=https://pcstudioabhi.com
MAIL_DEFAULT_SENDER=noreply@pcstudioabhi.com
```

---

### Step 4: Setup SSL Certificate

Use **Let's Encrypt** (Free):

```bash
# On your server
sudo apt-get install certbot python3-certbot-nginx

# Generate certificate
sudo certbot certonly --standalone -d pcstudioabhi.com -d www.pcstudioabhi.com

# Auto-renewal
sudo certbot renew --dry-run
```

---

### Step 5: Deploy Backend

**Use Gunicorn + Nginx:**

```bash
# Install production server
pip install gunicorn

# Run backend
gunicorn -w 4 -b 0.0.0.0:5000 server_v2:app
```

**Nginx Config:**
```nginx
server {
    listen 443 ssl http2;
    server_name api.pcstudioabhi.com;

    ssl_certificate /etc/letsencrypt/live/pcstudioabhi.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/pcstudioabhi.com/privkey.pem;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

# Redirect HTTP to HTTPS
server {
    listen 80;
    server_name api.pcstudioabhi.com;
    return 301 https://$server_name$request_uri;
}
```

---

### Step 6: Deploy Frontend

**On Web Host (Vercel, Netlify, or your server):**

```bash
# Build command
npm run build
# Or just serve the static files via Nginx
```

---

## 📧 Email Configuration

Update email sender to use custom domain:

```env
MAIL_DEFAULT_SENDER=support@pcstudioabhi.com
MAIL_FROM_NAME=PC Studio Abhi
```

**Setup SPF/DKIM/DMARC records:**

| Record | Value |
|--------|-------|
| SPF | `v=spf1 include:sendgrid.net ~all` |
| DKIM | Generate from mail provider |
| DMARC | `v=DMARC1; p=quarantine; rua=mailto:admin@pcstudioabhi.com` |

---

## 📊 Domain Architecture

```
pcstudioabhi.com (Frontend)
│
├─ www.pcstudioabhi.com (Alias)
├─ api.pcstudioabhi.com (Backend)
├─ admin.pcstudioabhi.com (Admin panel)
└─ mail.pcstudioabhi.com (Email)
```

---

## 🔒 SSL/HTTPS Setup

**Always use HTTPS in production!**

```bash
# Test SSL
curl -I https://pcstudioabhi.com

# Expected:
# HTTP/2 200
# Content-Type: text/html
```

---

## 📝 Update Frontend Configuration

Edit `js/app.js`:

```javascript
// Development
const API_URL = 'http://api.pcstudioabhi.com:5000/api';

// Production
const API_URL = 'https://api.pcstudioabhi.com/api';

// Or dynamic
const API_URL = window.location.hostname === 'localhost' 
    ? 'http://localhost:5000/api'
    : 'https://api.pcstudioabhi.com/api';
```

---

## 🎯 Checklist

### Local Development
- [ ] Edit hosts file
- [ ] Test domain resolves (ping pcstudioabhi.com)
- [ ] Access website via custom domain
- [ ] Update API URL in frontend

### Production
- [ ] Register domain
- [ ] Update DNS records
- [ ] Setup SSL certificate
- [ ] Deploy backend (Gunicorn)
- [ ] Deploy frontend (Nginx/Vercel)
- [ ] Setup email records (SPF/DKIM)
- [ ] Test HTTPS
- [ ] Configure email sender
- [ ] Setup monitoring

---

## 💰 Cost Breakdown

| Service | Cost | Notes |
|---------|------|-------|
| Domain | ₹300-500/year | One-time registration |
| Hosting | ₹300-5000/month | Depends on provider |
| SSL | Free | Let's Encrypt |
| Email | Free | Gmail or free tier |
| Total | ₹600-65000/year | Can be cheap! |

---

## 🚀 Popular Hosting Providers (India)

| Provider | Price | Features |
|----------|-------|----------|
| **Hostinger** | ₹149/month | VPS, unlimited, good support |
| **DigitalOcean** | $5-300/month | Cloud VPS, scalable |
| **AWS** | $0-1000/month | Enterprise, free tier |
| **Render** | Free-$7/month | Easy deployment, free tier |
| **Railway** | Free-$10/month | Modern hosting, simple |
| **Vercel** | Free-$20/month | Best for frontend |

---

## 📞 Email Setup

**Domain Email:**
```
support@pcstudioabhi.com
admin@pcstudioabhi.com
noreply@pcstudioabhi.com
```

**Setup Options:**
1. **Gmail for Business** - ₹600/user/month
2. **Zoho Mail** - Free (5 users)
3. **SendGrid** - Free (100/day)
4. **Mailgun** - Free tier available

---

## 🧪 Test Your Setup

```bash
# Test domain
nslookup pcstudioabhi.com

# Test SSL
openssl s_client -connect api.pcstudioabhi.com:443

# Test email
curl -X POST https://api.pcstudioabhi.com/api/health

# Full setup test
curl -X POST https://api.pcstudioabhi.com/api/products
```

---

## ✅ Success Indicators

✅ Domain resolves in browser  
✅ HTTPS shows green lock  
✅ API responds from custom domain  
✅ Emails send from custom domain  
✅ Admin panel accessible  
✅ Products load from API  
✅ Orders can be placed  

---

## 🆘 Troubleshooting

**Domain not resolving?**
- [ ] Check DNS propagation (24-48 hours)
- [ ] Clear browser cache
- [ ] Restart computer
- [ ] Verify DNS records are correct

**SSL certificate error?**
- [ ] Regenerate certificate
- [ ] Check certificate path in Nginx
- [ ] Verify domain in certificate

**API not responding?**
- [ ] Check Nginx configuration
- [ ] Verify backend is running
- [ ] Check firewall rules
- [ ] Review logs

---

## 📚 Resources

- **Domain Registration:** namecheap.com, godaddy.com
- **Hosting:** hostinger.com, digitalocean.com
- **SSL:** letsencrypt.org
- **Email:** zoho.com, sendgrid.com
- **Deployment:** vercel.com, render.com

---

## 🎉 Conclusion

You now have:
- ✅ Custom domain setup guide
- ✅ Local testing environment
- ✅ Production deployment steps
- ✅ Email configuration
- ✅ SSL setup instructions

**Next Steps:**
1. Choose hosting provider
2. Register domain
3. Setup DNS
4. Deploy application
5. Test everything
6. Go live!
