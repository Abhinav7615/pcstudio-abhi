# Second Hand PC Studio - Complete Setup & Usage Guide

## 🎯 Quick Start Guide

### Step 1: Open the Website
1. Navigate to your project folder: `c:\Users\ASUS\OneDrive\Desktop\Laptop`
2. Right-click on `index.html` and select "Open with Live Server"
3. The website will open in your default browser

### Step 2: Explore as a Customer
- Browse featured laptops on the home page
- Use filters to search by brand, price, or features
- Click "Add to Cart" to shop
- View your cart and proceed to checkout
- Complete your order with shipping details and payment method

### Step 3: Access Admin Dashboard
1. Click the "Login" button in the top navigation
2. Switch to the "Admin Login" tab
3. **Default Credentials**:
   - Username: `admin`
   - Password: `admin123` (or any password you set)
4. Click "Login" to access the admin dashboard

### Step 4: Admin Operations

#### View Dashboard
- See total orders, revenue, and inventory stats
- Monitor recent orders
- Quick access to all admin functions

#### Manage Products
1. Go to "Products" section
2. Click "Add New Product" button
3. Fill in product details:
   - Brand, Model
   - Processor, RAM, Storage specs
   - Condition (Excellent/Good/Fair)
   - Price & Original Price
   - Warranty period
   - Stock quantity
4. Click "Save Product"
5. View all products in the table below
6. Edit or Delete as needed

#### View Orders
1. Go to "Orders" section
2. See all customer orders with:
   - Order ID
   - Customer name and phone
   - Delivery address
   - Order amount
   - Payment method
   - Order status (pending/processing/completed)
   - Order date
3. Click "Update" to change order status
4. Click "View" to see full order details

#### Manage Customers
1. Go to "Customers" section
2. View all customers who placed orders
3. See customer contact information
4. Check number of orders per customer
5. Click "View" to see customer order history

#### Account Settings
1. Go to "Settings" section
2. Change admin username
3. Update password (requires current password)
4. Save settings

---

## 🛍️ Customer Experience Flow

### 1. **Browsing Products**
- Homepage displays 6 featured refurbished laptops
- Each product shows:
  - Brand and model
  - Specifications (processor, RAM, storage)
  - Condition badge (Excellent/Good/Fair)
  - Current price with discount percentage
  - Original price (strikethrough)
  - Customer rating and review count
  - Warranty period

### 2. **Filtering & Search**
- **Search Box**: Type laptop name or brand
- **Brand Filter**: Select from Dell, HP, Lenovo, ASUS, Apple
- **Price Filter**: Choose price range
- Results update in real-time

### 3. **Product Details**
- Click "View Details" on any product
- See full specifications
- Understand condition rating
- Check warranty coverage
- Review customer feedback

### 4. **Shopping Cart**
- Click "Add to Cart" to add products
- Success message appears
- Cart count updates in navbar
- Click cart icon to view items
- Remove items as needed
- See cart subtotal and total

### 5. **Checkout Process**
- Click "Proceed to Checkout"
- **Customer Information**:
  - Full name
  - Email address
  - Phone number
- **Shipping Address**:
  - Street address
  - Area/Locality
  - City
  - State (dropdown with all Indian states)
  - PIN code (6-digit validation)
- **Payment Method** (select one):
  - **UPI**: Enter UPI ID (e.g., username@bankname)
  - **Card**: Enter card details (number, expiry, CVV)
  - **Cash on Delivery**: No details needed
- Agree to Terms & Conditions
- Click "Place Order"

### 6. **Order Confirmation**
- Unique Order ID generated (e.g., ORDER-1707040123456)
- Confirmation popup appears
- Order details saved to local storage
- Can view order in admin dashboard

---

## 🔐 Authentication System

### Customer Login/Registration

#### Register as New Customer
1. Click "Login" button
2. Go to "Register" tab
3. Enter:
   - Full Name
   - Email address
   - Phone number
   - Password (minimum 6 characters)
   - Confirm password
4. Check "I agree to Terms & Conditions"
5. Click "Register"

#### Login with Email & Password
1. Click "Login" button
2. Go to "Login" tab (default)
3. Enter:
   - Email address
   - Password
4. Click "Login"

#### Login with OTP (Customer)
1. Click "Login" button
2. Go to "Login" tab
3. Click "Login with OTP" button
4. Enter phone number
5. Click "Send OTP" (will show alert about backend integration)
6. Enter 4-digit OTP when received
7. Click "Verify OTP"

### Admin Login/Registration

#### Standard Admin Login
1. Click "Login" button
2. Go to "Admin Login" tab
3. Enter:
   - Admin username: `admin`
   - Password: `admin123` (customizable)
4. Click "Login"

#### Admin OTP Login
1. Click "Login" button
2. Go to "Admin Login" tab
3. Click "Login with OTP" button
4. Enter:
   - Admin username
   - Registered phone number (6388391842)
5. Click "Send OTP"
6. Enter 4-digit OTP
7. Click "Verify OTP"

---

## 📦 Order Management (Admin)

### Viewing Orders
1. Navigate to admin dashboard
2. Orders appear in the "Recent Orders" section on dashboard
3. Go to "Orders" tab for complete order list

### Order Information Captured
- **Order ID**: Unique identifier
- **Customer Details**: Name, email, phone
- **Shipping Address**: Full address with state and PIN code
- **Order Items**: List of laptops with quantities
- **Amount**: Subtotal, GST (18%), Total
- **Payment Method**: UPI/Card/COD
- **Order Status**: Pending/Processing/Completed
- **Order Date**: When order was placed

### Updating Order Status
1. Find the order in the Orders tab
2. Click "Update" button
3. Enter new status:
   - `pending`: Order received, awaiting confirmation
   - `processing`: Order confirmed, being prepared
   - `completed`: Order shipped/delivered
4. Status updates immediately

### Viewing Order Details
1. Click "View" button for any order
2. See complete order information popup
3. Includes all customer details and items

---

## 📊 Admin Statistics

### Dashboard Metrics
1. **Total Orders**: All orders placed
2. **Pending Orders**: Orders awaiting confirmation/processing
3. **Total Revenue**: Sum of all order amounts
4. **Total Products**: Number of laptops in inventory

### Recent Orders Widget
- Shows last 5 orders
- Quick view and update buttons
- Order status at a glance

---

## 💳 Payment Methods

### UPI Payment
- **Process**: Real-time digital transfer
- **Details Needed**: UPI ID (username@bankname)
- **Speed**: Instant
- **Fees**: Usually free

### Card Payment
- **Types Accepted**: Debit card, Credit card, RuPay
- **Details Needed**: 
  - Cardholder name
  - Card number (16 digits)
  - Expiry date (MM/YY)
  - CVV (3 digits)
- **Security**: Encrypted during checkout
- **Processing**: Immediate

### Cash on Delivery (COD)
- **Process**: Pay upon delivery
- **Amount**: Collected by courier
- **Benefit**: No advance payment needed
- **Delivery**: Standard delivery timeline applies

---

## 🔄 Return & Refund Process

### Eligibility
- Within 15 days from delivery date
- Laptop in original condition
- Original packaging and accessories included
- No physical damage or water exposure
- Valid order ID required

### Return Steps
1. Contact via WhatsApp: +91 6388391842
2. Provide order ID and reason
3. Get return authorization
4. Receive return shipping label
5. Ship product back securely
6. We inspect upon receipt
7. Refund processed within 5-7 business days

### Refund Options
- **Full Refund**: If product is defective
- **Partial Refund**: If minor damage from shipping
- **Replacement**: If customer prefers new unit

---

## 🏠 Pages & Sections

### Main Pages
| Page | URL | Purpose |
|------|-----|---------|
| Home | `index.html` | Featured products & shopping |
| Checkout | `pages/checkout.html` | Order placement |
| Admin | `pages/admin.html` | Admin management |

### Information Pages
| Page | URL | Purpose |
|------|-----|---------|
| About | `pages/about.html` | Company info & mission |
| Contact | `pages/contact.html` | Contact form & support |
| Return Policy | `pages/return-policy.html` | 15-day returns |
| Warranty | `pages/warranty.html` | Warranty details |
| Privacy | `pages/privacy.html` | Data privacy |
| Terms | `pages/terms.html` | Terms of service |

---

## 📞 Support Channels

### Direct Contact
- **Phone**: +91 6388391842
- **Email**: info@secondhandpc.com
- **WhatsApp**: Click WhatsApp button on site

### Business Hours
- **Monday to Sunday**: 10:00 AM - 8:00 PM (IST)
- **Holidays**: By appointment

### FAQ Page Features
- How long does delivery take?
- Accepted payment methods
- Warranty coverage details
- Return policy overview
- Product authenticity assurance

---

## 🔧 Troubleshooting

### Cart Issues
**Problem**: Items not staying in cart
**Solution**: Clear browser cache and cookies, try again

**Problem**: Cart count not updating
**Solution**: Refresh the page after adding items

### Login Issues
**Problem**: Admin login not working
**Solution**: Check if admin account is properly set up in settings

**Problem**: Customer login errors
**Solution**: Verify email and password are correct

### Order Issues
**Problem**: Orders not appearing in admin dashboard
**Solution**: Check browser console for errors, reload page

**Problem**: Cannot complete checkout
**Solution**: Ensure all fields are filled correctly, verify pin code format

---

## 💡 Tips for Admin

1. **Add Products First**: Before opening to customers, populate the inventory
2. **Monitor Orders Daily**: Check for new orders and update status
3. **Respond Quickly**: Answer customer queries within 24 hours
4. **Update Status**: Keep customers informed about order progress
5. **Check Revenue**: Monitor total revenue and pending orders
6. **Manage Stock**: Keep track of available inventory
7. **Backup Data**: Regularly save order data

---

## 📈 Customer Tips

1. **Use Filters**: Narrow down laptop options efficiently
2. **Check Reviews**: See ratings from other customers
3. **Read Details**: Understand specifications before buying
4. **Compare Prices**: Check different conditions for same model
5. **Contact Support**: Reach out via WhatsApp for questions
6. **Track Order**: Monitor order status after purchase
7. **Return Easy**: Use 15-day return policy if not satisfied

---

## 🎨 Customization Notes

### Change Company Details
Update in all files:
- Company name in navbar
- Phone numbers: 6388391842
- Email: info@secondhandpc.com
- WhatsApp link: https://wa.me/916388391842

### Update Colors
Edit in `css/style.css`:
- `:root` color variables
- Primary color: #2c3e50
- Secondary color: #e74c3c

### Add/Remove Products
Use Admin Dashboard → Products section to:
- Add new laptops with specifications
- Set prices and stock
- Update availability
- Remove discontinued items

---

## 📱 Mobile Optimization

The website is fully responsive:
- **Desktop**: Full feature set (1024px+)
- **Tablet**: Optimized layout (768px)
- **Mobile**: Touch-friendly design (480px)
- **Very Small**: Extra small screens (320px)

---

**Version**: 1.0 (Frontend Complete)
**Last Updated**: February 2, 2026
**Status**: Ready for Frontend Use + Backend Integration

For backend setup (Node.js, Database, SMS, Payments), refer to the main README.md file.
