# 🎨 Visual Guide - Second Hand PC Studio

## Website Layout Overview

### Homepage (index.html)
```
┌─────────────────────────────────────────────┐
│  🏢 Second Hand PC Studio      [Login] [🛒] │ ← Navbar
├─────────────────────────────────────────────┤
│                                             │
│  Quality Refurbished Laptops                │ ← Hero Section
│  Affordable, Reliable, and Fully Tested     │
│         [Shop Now Button]                   │
│                                             │
├─────────────────────────────────────────────┤
│  ✓ Quality    ✓ Warranty   ✓ Returns  ✓ Help │ ← Trust Badges
├─────────────────────────────────────────────┤
│  Featured Laptops                           │
│  Search: [___________] Brand: [___] Price: [___] │
│                                             │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐    │
│  │ Dell    │  │ HP      │  │ Lenovo  │    │ ← Product Cards
│  │ Latitude│  │EliteBook│  │ThinkPad │    │
│  │ ₹35,000 │  │ ₹45,000 │  │ ₹28,000 │    │
│  │ [Add]   │  │ [Add]   │  │ [Add]   │    │
│  └─────────┘  └─────────┘  └─────────┘    │
│                                             │
├─────────────────────────────────────────────┤
│  Customer Reviews                           │
│  ⭐⭐⭐⭐⭐ "Excellent quality!" - Rajesh    │ ← Reviews
│  ⭐⭐⭐⭐  "Great value" - Priya             │
│  ⭐⭐⭐⭐⭐ "Highly recommended!" - Amit     │
│                                             │
├─────────────────────────────────────────────┤
│  📞 WhatsApp Support                        │ ← CTA
│  [Chat on WhatsApp]                         │
│                                             │
├─────────────────────────────────────────────┤
│  © 2026 Second Hand PC Studio               │ ← Footer
│  Return Policy | Warranty | Contact         │
└─────────────────────────────────────────────┘
```

---

## Shopping Flow Diagram

```
START
  ↓
[Homepage] - Browse Products
  ↓
[Search & Filter] - Narrow Results
  ↓
[View Details] - Check Specs
  ↓
[Add to Cart] - 1 or more items
  ↓
[View Cart] - Review items
  ↓
[Checkout] - Shipping & Payment
  ├─ Enter Address
  ├─ Select Payment
  └─ Agree to Terms
  ↓
[Place Order] - Get Order ID
  ↓
[Confirmation] - Order saved
  ↓
END
```

---

## Admin Dashboard Flow

```
START
  ↓
[Login Page]
  ├─ Username: admin
  └─ Password: admin123
  ↓
[Admin Dashboard]
  ├─────────────────────────
  │ Dashboard Stats:
  │  • Total Orders: 5
  │  • Pending: 2
  │  • Revenue: ₹180,000
  │  • Products: 20
  ├─────────────────────────
  ├─ Products
  │  ├─ Add New
  │  ├─ Edit
  │  └─ Delete
  ├─ Orders
  │  ├─ View Details
  │  └─ Update Status
  ├─ Customers
  │  └─ View Profile
  └─ Settings
     ├─ Change Username
     ├─ Change Password
     └─ Clear Data
  ↓
END
```

---

## Page Navigation Map

```
index.html (Homepage)
├─ [Products Link] → #products
├─ [About Link] → pages/about.html
├─ [Contact Link] → pages/contact.html
├─ [Login] → Auth Modal
│  ├─ Customer Login Tab
│  ├─ Customer Register Tab
│  └─ Admin Login Tab
├─ [Shopping Cart] → Cart Modal
└─ [WhatsApp] → https://wa.me/916388391842

pages/checkout.html
├─ [Home Link] → index.html
├─ [Back Link] → Previous Page

pages/admin.html
├─ [Dashboard] → Dashboard Section
├─ [Orders] → Orders Section
├─ [Products] → Products Section
├─ [Customers] → Customers Section
├─ [Settings] → Settings Section
└─ [Logout] → Redirects to index.html

pages/about.html
├─ [Home] → index.html
├─ [Products] → index.html#products

pages/contact.html
├─ [Home] → index.html
├─ [Contact Form] → Email Alert
└─ [FAQ Section] → Expand/Collapse

pages/return-policy.html
pages/warranty.html
pages/privacy.html
pages/terms.html
└─ [Home] → index.html
```

---

## Responsive Breakpoints

```
Desktop (1024px+)
┌──────────────────────────────────┐
│ Full Navigation Bar              │
│ 4-Column Product Grid            │
│ 2-Column Layout (Checkout)        │
│ Sidebar Menu (Admin)             │
└──────────────────────────────────┘

Tablet (768px)
┌──────────────────────┐
│ Hamburger Menu       │
│ 2-Column Grid        │
│ Stacked Layout       │
└──────────────────────┘

Mobile (480px)
┌──────────────────┐
│ Hamburger Menu   │
│ 1-Column Grid    │
│ Full Width Forms │
└──────────────────┘

Extra Small (320px)
┌──────────┐
│ Compact  │
│ Minimal  │
│ Touch    │
└──────────┘
```

---

## Color Scheme

```
PRIMARY: #2c3e50 (Dark Blue)
Used for: Navbar, Headers, Text

SECONDARY: #e74c3c (Red/Orange)
Used for: Buttons, Highlights, Warnings

ACCENT: #3498db (Light Blue)
Used for: Links, Secondary buttons

SUCCESS: #27ae60 (Green)
Used for: Positive messages, Checks

WARNING: #f39c12 (Orange)
Used for: Ratings, Cautions

LIGHT BG: #ecf0f1 (Light Gray)
Used for: Section backgrounds

TEXT DARK: #2c3e50
Used for: Main text

TEXT LIGHT: #7f8c8d
Used for: Secondary text
```

---

## Product Card Details

```
┌──────────────────┐
│   💻 (Emoji)     │ ← Product Image
│   [DISCOUNT %]   │ ← Badge
├──────────────────┤
│ Brand Model      │ ← Title
│                  │
│ Processor: xxx   │ ← Specs
│ RAM: xxx         │
│ Storage: xxx     │
│                  │
│ [Good Condition] │ ← Condition Badge
│ ⭐4.5 (24 reviews)│ ← Rating
│                  │
│ ₹35,000 ₹45,000 │ ← Pricing
│ [Add to Cart] 🛒 │ ← Action Buttons
│ [View Details]   │
└──────────────────┘
```

---

## Checkout Form Layout

```
CHECKOUT PAGE
┌────────────────────────────────────────────┐
│ [Back] Checkout                            │
├────────────────────────────────────────────┤
│                                            │
│  LEFT COLUMN          │  RIGHT COLUMN      │
│  ─────────────────    │  ────────────────  │
│  Customer Info        │  Order Summary     │
│  [Name]               │  Item 1: ₹35,000   │
│  [Email]              │  Item 2: ₹45,000   │
│  [Phone]              │  ─────────────     │
│                       │  Subtotal: ₹80k    │
│  Shipping Address     │  Tax: ₹14.4k       │
│  [Address]            │  Total: ₹94.4k     │
│  [Area]               │                    │
│  [City]               │  ℹ️ Shipping Info  │
│  [State]              │  ✓ Free shipping   │
│  [PIN Code]           │  ✓ 2-3 days       │
│                       │                    │
│  Payment Method       │  🛡️ Returns Policy│
│  ⦿ UPI               │  ✓ 15-day return   │
│  ○ Card              │                    │
│  ○ Cash on Delivery  │                    │
│                       │                    │
│  [I agree to Terms]   │  [Place Order]     │
│                       │                    │
└────────────────────────────────────────────┘
```

---

## Admin Dashboard Layout

```
┌────────────────────────────────────────────────────────┐
│                  ADMIN SIDEBAR      │   MAIN CONTENT   │
│  ┌──────────────┐                  │ ┌──────────────┐ │
│  │ Admin Panel  │                  │ │ Dashboard    │ │
│  ├──────────────┤                  │ ├──────────────┤ │
│  │ 👤 Admin     │                  │ │              │ │
│  │ Admin User   │                  │ │ [Stats Cards]│ │
│  │ Admin        │                  │ │ - Orders: 5  │ │
│  │              │                  │ │ - Revenue: ₹ │ │
│  │ 📊 Dashboard │                  │ │              │ │
│  │ 📦 Orders    │                  │ │ [Orders Table]
│  │ 💻 Products  │                  │ │              │ │
│  │ 👥 Customers │                  │ │              │ │
│  │ ⚙️ Settings  │                  │ │              │ │
│  │              │                  │ │              │ │
│  │ [Logout]     │                  │ │              │ │
│  │              │                  │ │              │ │
│  └──────────────┘                  │ └──────────────┘ │
│                                    │                  │
└────────────────────────────────────────────────────────┘
```

---

## Auth Modal Tabs

```
┌─────────────────────────────────┐
│ [Login] [Register] [Admin]       │ ← Tab Buttons
├─────────────────────────────────┤
│                                 │
│ Customer Login                  │
│                                 │
│ [Email:]                        │
│ [_____________________]         │
│                                 │
│ [Password:]                     │
│ [_____________________]         │
│                                 │
│ [Login Button]                  │
│ ─────── OR ───────              │
│ [Login with OTP]                │
│                                 │
└─────────────────────────────────┘
```

---

## Mobile Navigation

```
MOBILE MENU (Open)
┌──────────────────────┐
│ 🏢 Company Name      │
│ ☰ Menu              │
├──────────────────────┤
│ Home                 │
│ Products             │
│ About                │
│ Contact              │
│ [Login]              │
│ [🛒 Cart]            │
└──────────────────────┘

MOBILE MENU (Closed)
┌──────────────────────┐
│ 🏢 Company   ☰ [🛒] │
└──────────────────────┘
```

---

## Form Validation States

```
✓ VALID (Green)
┌─────────────┐
│ [Email] ✓   │ ← Green checkmark
│ Email is OK │
└─────────────┘

✗ INVALID (Red)
┌─────────────┐
│ [Email] ✗   │ ← Red X
│ Invalid email
└─────────────┘

ⓘ INFO (Blue)
┌─────────────┐
│ [Email] ⓘ   │ ← Info icon
│ Required    │
└─────────────┘
```

---

## Success/Error Messages

```
✓ SUCCESS MESSAGE
┌────────────────────────┐
│ ✓ Added to cart!       │ ← Green bg
│                        │
└────────────────────────┘

✗ ERROR MESSAGE
┌────────────────────────┐
│ ✗ Please fill all      │ ← Red bg
│   required fields      │
└────────────────────────┘

ⓘ INFO MESSAGE
┌────────────────────────┐
│ ⓘ Processing order...  │ ← Blue bg
│                        │
└────────────────────────┘
```

---

## Data Flow Diagram

```
Customer enters data
        ↓
Form validation (Client-side)
        ↓
Data stored in localStorage
        ↓
Admin can view in dashboard
        ↓
Admin updates order status
        ↓
Status persists in localStorage
        ↓
Customer notified (Future: Email/SMS)
```

---

## Browser Compatibility

```
✓ Chrome (Latest)      [Full Support]
✓ Firefox (Latest)     [Full Support]
✓ Safari (Latest)      [Full Support]
✓ Edge (Latest)        [Full Support]
✓ Mobile Chrome        [Full Support]
✓ Mobile Safari        [Full Support]
⚠ IE 11                [Limited Support]
```

---

This visual guide helps understand the structure and layout of the entire Second Hand PC Studio website!

**Version**: 1.0
**Last Updated**: February 2, 2026
