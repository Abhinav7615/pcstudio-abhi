# Website Configuration

## 🌐 Website Name & Domain Setup

### Current Setup
- **Website Name**: Second Hand PC Studio
- **Frontend**: Running on `http://localhost:5500` (Live Server)
- **Backend API**: Running on `http://localhost:5000` (Flask)

### To Setup Custom Domain (secondhandpcstudio.com or similar)

#### Option 1: Using Hosts File (Local Testing)
1. Edit `C:\Windows\System32\drivers\etc\hosts` (as Administrator)
2. Add this line:
```
127.0.0.1    secondhandpcstudio.local
127.0.0.1    api.secondhandpcstudio.local
```

3. Then access:
   - Frontend: `http://secondhandpcstudio.local:5500`
   - API: `http://api.secondhandpcstudio.local:5000`

#### Option 2: Update API URL in Code
Edit the API URL in [js/app.js](js/app.js):
```javascript
// Change this line:
const API_URL = 'http://localhost:5000/api';

// To your custom domain:
const API_URL = 'http://secondhandpcstudio.com/api';
```

#### Option 3: Deploy to Web Host
Follow these steps for production deployment:

1. **Get a Domain**: Purchase from GoDaddy, Namecheap, etc.
2. **Choose Hosting**: Use services like:
   - Heroku (for backend)
   - Netlify (for frontend)
   - AWS, Azure, or DigitalOcean

3. **Setup Environment Variables**:
   - Set `API_URL` to your production backend URL
   - Configure CORS for your domain

4. **Deploy**:
   - Push backend code to Heroku
   - Push frontend code to Netlify
   - Point domain DNS to your hosting provider

### Environment Files for Different Stages

Create a `.env` file in the root directory:
```
ENVIRONMENT=development
API_URL=http://localhost:5000/api
WEBSITE_NAME=Second Hand PC Studio
```

For production, update to:
```
ENVIRONMENT=production
API_URL=https://api.secondhandpcstudio.com
WEBSITE_NAME=Second Hand PC Studio
```

---

**Your website is ready! 🚀**
