# Second Hand PC Studio - E-Commerce Website

A complete e-commerce website for selling refurbished laptops with customer and admin functionalities.

## 🚀 Features

### Customer Features
- **Product Browsing**: Filter and search laptops by brand, price, condition
- **Product Details**: Detailed specifications (processor, RAM, storage, warranty, condition)
- **Customer Reviews**: View ratings and reviews from other customers
- **Shopping Cart**: Add/remove products, view cart summary
- **Checkout System**: Complete checkout with shipping address and payment options
- **Payment Methods**: UPI, Card, and Cash on Delivery (COD)
- **Order Tracking**: Order confirmation and status tracking
- **Customer Authentication**: Login/Registration with email and phone
- **OTP Verification**: 4-digit OTP for secure login
- **Return Policy**: Easy 15-day return and refund policy
- **WhatsApp Contact**: Direct WhatsApp integration for support

### Admin Features
- **Admin Dashboard**: Overview of orders, revenue, and inventory
- **Order Management**: View and update order status
- **Product Management**: Add, edit, delete products with stock management
- **Customer Management**: View customer information and order history
- **Account Settings**: Change username, password via OTP verification
- **Data Management**: Clear all data and perform admin tasks

## 📋 Website Structure

```
Laptop/
├── index.html                    # Home page with product listing
├── css/
│   ├── style.css               # Main stylesheet
│   └── responsive.css          # Mobile responsive styles
├── js/
│   ├── app.js                  # Main application logic
│   ├── auth.js                 # Authentication functions
│   └── cart.js                 # Shopping cart management
├── pages/
│   ├── checkout.html           # Checkout page
│   ├── admin.html              # Admin dashboard
│   ├── about.html              # About us
│   ├── contact.html            # Contact page
│   ├── return-policy.html      # Return & refund policy
│   ├── warranty.html           # Warranty information
│   ├── privacy.html            # Privacy policy
│   ├── terms.html              # Terms & conditions
│   └── assets/                 # Images and media
└── backend/                    # Backend server setup (Node.js)
```

## 🔐 Admin Login Credentials

**Default Admin Setup**:
- **Username**: admin
- **Phone**: 6388391842
- **Access**: Admin Dashboard at `/pages/admin.html`

**Login Methods**:
1. **Username & Password**: Traditional login
2. **OTP Login**: 4-digit OTP sent via SMS (for backend integration)

## 💳 Payment Options

1. **UPI**: Fast and secure digital payment
2. **Card**: Debit/Credit card payments (Visa, Mastercard, RuPay)
3. **Cash on Delivery**: Pay when you receive the laptop

## 🛒 Shopping Features

### Product Filtering
- Search by name or model
- Filter by brand (Dell, HP, Lenovo, ASUS, Apple)
- Filter by price range
- Condition: Excellent, Good, Fair

### Product Information Displayed
- Brand and Model
- Processor, RAM, Storage specifications
- Product condition with color-coded badges
- Price with discount percentage
- Customer rating and review count
- Warranty period
- Add to cart button

### Cart & Checkout
- View cart with itemized list
- Update quantities
- Remove items
- Shipping address form with pincode validation
- Order summary with GST calculation
- Order confirmation with order ID

## 👥 Customer Account Features

### Registration
- Full name, email, phone number
- Password creation (minimum 6 characters)
- Terms & conditions acceptance

### Login Options
1. **Email & Password**
2. **Phone OTP** (4-digit, SMS-based)

### Account Management
- Change password via OTP verification
- Update profile information
- View order history
- Track deliveries

## 📞 Customer Support

- **Phone**: +91 6388391842
- **WhatsApp**: Direct chat integration
- **Email**: info@secondhandpc.com
- **Hours**: 10 AM - 8 PM (IST), Daily
- **FAQ**: Available on contact page

## 🔧 Technology Stack

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Flexbox, Grid, responsive design
- **JavaScript**: Vanilla JS (no frameworks)
- **FontAwesome**: Icons

### Storage & Data
- **LocalStorage**: Customer data, cart, orders (Client-side)
- **SessionStorage**: Admin login session

### Backend Requirements (To be implemented)
- **Node.js/Express** or **Python/Django**
- **MongoDB** or **PostgreSQL**
- **SMS Gateway**: Twillio or similar for OTP
- **Payment Gateway**: Razorpay, PayU, or similar
- **Email Service**: SendGrid or similar

## 📱 Responsive Design

- **Desktop**: Full-featured interface
- **Tablet**: Optimized layout (768px breakpoint)
- **Mobile**: Touch-friendly design (480px breakpoint)
- **Extra Small**: Devices below 320px

## 🎯 Key Pages

| Page | Purpose |
|------|---------|
| `index.html` | Home page with featured products |
| `/pages/checkout.html` | Order placement |
| `/pages/admin.html` | Admin dashboard |
| `/pages/about.html` | Company information |
| `/pages/contact.html` | Contact form & FAQ |
| `/pages/return-policy.html` | 15-day return policy |
| `/pages/warranty.html` | Warranty details |
| `/pages/privacy.html` | Data privacy policy |
| `/pages/terms.html` | Terms & conditions |

## 🚀 Getting Started

### 1. **Local Setup**
```bash
# Navigate to project folder
cd Laptop

# Open in browser (or use Live Server in VS Code)
# Right-click index.html > Open with Live Server
```

### 2. **Admin Access**
- Click "Login" button on homepage
- Switch to "Admin Login" tab
- Use default credentials to login

### 3. **Add Products** (Admin)
- Go to Products section in admin dashboard
- Click "Add New Product"
- Fill in product details
- Click "Save Product"

### 4. **View Orders** (Admin)
- Check "Orders" section in admin dashboard
- All customer orders with details appear here
- Update order status as needed

## 💾 Data Storage

### LocalStorage Keys
- `cart`: Shopping cart items
- `orders`: All customer orders
- `products`: Product catalog (Admin managed)
- `customers`: Customer accounts (for future backend integration)

### SessionStorage Keys
- `adminLoggedIn`: Admin login status
- `adminUsername`: Current admin name
- `customerLoggedIn`: Customer login status

## 🔐 Security Features

- **256-bit SSL Encryption** (To be implemented in backend)
- **PCI DSS Compliance** (Payment processing)
- **Secure Password Hashing** (Backend implementation needed)
- **OTP Verification** (SMS-based, backend needed)
- **Session Management**: Auto-logout after inactivity
- **Form Validation**: Client-side validation on all forms

## 📊 Admin Dashboard Widgets

- **Total Orders**: Count of all orders
- **Pending Orders**: Orders awaiting confirmation
- **Total Revenue**: Sum of all order amounts
- **Total Products**: Number of products in inventory
- **Recent Orders**: Last 5 orders with details

## 🛠️ Future Enhancements

- [ ] Backend API with Node.js/Express
- [ ] Database integration (MongoDB/PostgreSQL)
- [ ] Real SMS OTP service integration
- [ ] Payment gateway integration
- [ ] Email notifications
- [ ] Real-time order tracking
- [ ] Customer analytics
- [ ] Inventory alerts
- [ ] Product recommendations
- [ ] Advanced search & filters
- [ ] Social media integration
- [ ] Mobile app version

## 📝 Default Sample Data

The website comes with 6 sample laptops:
1. Dell Latitude 5420 - ₹35,000
2. HP EliteBook 840 G8 - ₹45,000
3. Lenovo ThinkPad E15 - ₹28,000
4. ASUS VivoBook 15 - ₹42,000
5. Dell XPS 13 - ₹65,000
6. HP Pavilion 15 - ₹22,000

And 6 sample customer reviews.

## 🎨 Color Scheme

- **Primary**: #2c3e50 (Dark Blue)
- **Secondary**: #e74c3c (Red)
- **Accent**: #3498db (Blue)
- **Success**: #27ae60 (Green)
- **Warning**: #f39c12 (Orange)
- **Light BG**: #ecf0f1 (Light Gray)

## 📧 Contact Information

**Second Hand PC Studio**
- Phone: +91 6388391842
- WhatsApp: https://wa.me/916388391842
- Email: info@secondhandpc.com
- Hours: 10 AM - 8 PM (IST), Daily

## 📄 License

This is a custom project for Second Hand PC Studio. All rights reserved.

## 🤝 Support

For technical support or inquiries, contact the admin at the numbers or email provided above.

---

**Last Updated**: February 2, 2026
**Version**: 1.0 (Frontend Complete, Backend to be implemented)
