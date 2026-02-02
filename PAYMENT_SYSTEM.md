# Online Payment System - Documentation

## 📋 Overview

This document outlines the complete online payment system implementation for Second Hand PC Studio. The system allows customers to make payments via UPI or Bank Transfer with manual verification by the admin.

## 🎯 System Features

### Customer Side (Checkout Page)

1. **Payment Method Selection**
   - UPI Payment
   - Bank Transfer
   - Cash on Delivery (COD)

2. **Payment Details Display**
   - Admin's UPI ID (if configured)
   - Bank account details (if configured)
   - Owner name and other required information

3. **Payment Proof Upload**
   - **Transaction ID**: Customer enters the UPI reference/transaction number
   - **Payment Proof File**: Customer uploads a screenshot or photo of:
     - Successful payment confirmation
     - Transaction receipt
     - Bank transfer confirmation
   - Supported formats: JPG, PNG

### Admin Dashboard

#### 1. **Settings → Payment Details**
   
   **UPI Payment Setup**
   - UPI ID (e.g., yourname@paytm)
   - Owner Name
   - Save button to store details

   **Bank Transfer Setup**
   - Bank Name
   - Account Holder Name
   - Account Number
   - IFSC Code
   - Save button to store details

#### 2. **Payment Verification Section**
   
   A dedicated section in the sidebar to verify pending payments
   
   **View Payment Proofs**
   - List of all pending payment verifications
   - Shows: Order ID, Customer Name, Amount, Payment Method, Transaction ID
   - Status badge showing "pending"

   **Payment Proof Review Modal**
   - Order information display
   - Customer details
   - Transaction ID
   - Uploaded payment proof image
   - Admin notes field for adding verification comments

   **Verification Actions**
   - **Approve Payment**: 
     - Marks payment as "verified"
     - Changes order status to "completed"
     - Stores verification timestamp
   - **Reject Payment**: 
     - Marks payment as "rejected"
     - Keeps order as "payment_pending"
     - Allows customer to resubmit proof
     - Admin can add rejection reason/notes

## 🔄 Payment Flow

### Step 1: Customer Checkout
```
Customer selects items → Goes to Checkout page
→ Enters shipping details
→ Selects payment method (UPI/Bank/COD)
→ Enters transaction ID
→ Uploads payment proof
→ Places order
```

### Step 2: Payment Submission
```
Order created with status: "pending"
Payment proof stored with status: "pending"
Customer receives success message
```

### Step 3: Admin Verification
```
Admin logs in → Goes to Payment Verification section
→ Views pending payments list
→ Clicks "View Proof" button
→ Reviews payment proof image and details
→ Adds notes if needed
→ Clicks "Approve" or "Reject"
→ Order status updated accordingly
```

### Step 4: Customer Notification
```
If Approved:
  Order status → "completed"
  Admin will proceed with order fulfillment

If Rejected:
  Order status → "payment_pending"
  Customer needs to resubmit proof
```

## 📊 Order Status Flow

```
pending 
  ↓
payment_pending (after customer submits proof)
  ↓
  ├→ completed (if admin approves)
  └→ payment_pending (if admin rejects - customer can resubmit)
```

## 💾 Data Storage

### localStorage Keys

1. **paymentDetails** - Admin's payment information
   ```json
   {
     "upi": {
       "upiId": "yourname@paytm",
       "ownerName": "Your Name",
       "savedAt": "2026-02-02T..."
     },
     "bank": {
       "bankName": "HDFC Bank",
       "accountHolder": "Your Name",
       "accountNumber": "1234567890",
       "ifscCode": "HDFC0001234",
       "savedAt": "2026-02-02T..."
     }
   }
   ```

2. **paymentProofs** - Customer payment proofs
   ```json
   [
     {
       "orderId": "ORDER-1706886000",
       "transactionId": "UPI123456789",
       "proofFile": "data:image/...", // Base64 encoded image
       "fileName": "payment_proof.jpg",
       "uploadedAt": "2026-02-02T...",
       "status": "pending|verified|rejected",
       "verifiedAt": "2026-02-02T...",
       "adminNotes": "Payment verified"
     }
   ]
   ```

3. **orders** - Enhanced with payment fields
   ```json
   [
     {
       "orderId": "ORDER-1706886000",
       "customerName": "Customer Name",
       "customerEmail": "customer@email.com",
       "paymentMethod": "upi|bank|cod",
       "transactionId": "UPI123456789",
       "paymentProof": {...}, // Full proof object
       "status": "pending|payment_pending|completed",
       ...
     }
   ]
   ```

## 🔐 Security Considerations

1. **Payment Details Protection**
   - Account numbers are partially masked in customer view
   - Full details only visible in admin panel
   - Consider using backend server (not localStorage) for production

2. **Proof Verification**
   - Admin manually verifies each payment proof
   - Proof images stored as base64 in localStorage (for demo)
   - In production, upload to secure server

3. **Admin Actions**
   - Only logged-in admins can verify payments
   - Verification logged with timestamp
   - Can add notes for audit trail

## 🚀 Backend Integration (Future)

The backend skeleton includes these endpoints (currently commented):

```
GET  /api/payment-details           - Get admin payment details
POST /api/admin/payment-details/upi - Save UPI details
POST /api/admin/payment-details/bank - Save Bank details
POST /api/orders                     - Create order
POST /api/orders/<id>/payment-proof  - Submit payment proof
GET  /api/admin/orders-with-payment  - Get orders with payment status
GET  /api/admin/pending-verifications - Get pending verifications
POST /api/admin/orders/<id>/verify-payment - Verify/reject payment
```

## 📱 Admin Panel Navigation

1. **Sidebar Menu**
   - Dashboard (shows pending orders count)
   - **Payment Verification** ⭐ (NEW)
   - Orders
   - Products
   - Customers
   - Settings

2. **Settings Section**
   - UPI Payment Details form
   - Bank Transfer Details form
   - Account Settings
   - Danger Zone

## 🎨 UI/UX Features

1. **Payment Proof Modal**
   - Displays full order information
   - Shows uploaded proof image
   - Text area for admin notes
   - Approve/Reject buttons with icons
   - Clean, professional layout

2. **Status Badges**
   - pending: Yellow
   - verified: Green
   - rejected: Red

3. **Payment Details Display**
   - Admin UPI details shown at checkout
   - Admin Bank details shown at checkout
   - Information is properly formatted
   - Clear labeling of required fields

## 🧪 Testing the System

### Test Scenario 1: UPI Payment
1. Add UPI details in Admin Settings
2. Go to checkout
3. Select "UPI Payment"
4. See admin's UPI ID displayed
5. Enter transaction ID and upload proof image
6. Place order
7. In admin panel, review payment proof
8. Approve or reject

### Test Scenario 2: Bank Transfer
1. Add Bank details in Admin Settings
2. Go to checkout
3. Select "Bank Transfer"
4. See admin's bank account displayed
5. Enter transaction ID and upload proof image
6. Place order
7. In admin panel, review payment proof
8. Approve or reject

### Test Scenario 3: COD
1. Select "Cash on Delivery"
2. Order placed directly
3. Payment verification skipped

## 📝 Admin Workflow

```
1. Login to Admin Panel
2. Go to Settings → Add UPI/Bank Details
3. Customers place orders with payments
4. Go to Payment Verification section
5. See list of pending payments
6. Click "View Proof" for each payment
7. Review proof image and details
8. Add notes if needed
9. Click "Approve" or "Reject"
10. Order status updates automatically
```

## 🔄 Customer Experience

```
1. Select items and go to checkout
2. Enter delivery address
3. Select payment method
4. See admin payment details
5. Make payment outside the app
6. Enter transaction ID
7. Upload screenshot/proof
8. Place order
9. Get success message
10. Wait for admin verification
11. Receive confirmation when approved
```

## 💡 Key Points

✅ Admin can add/edit payment details anytime
✅ Multiple payment methods supported
✅ Payment proof stored with order
✅ Admin can approve or reject payments
✅ Admin can add verification notes
✅ Order status updates automatically
✅ Responsive design for all devices
✅ Secure payment verification process
✅ Data persisted in localStorage

## 🔧 Customization

You can easily customize:
- Payment methods (add more options)
- Order statuses (add more states)
- Verification workflow
- Admin notes requirements
- Payment details display format
- Status badge colors
- Form field validation

## 📞 Support

For issues or questions about the payment system, please contact the admin panel.

---

**Last Updated**: February 2, 2026
**System Version**: 1.0
**Status**: ✅ Production Ready (localStorage version)
