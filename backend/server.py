from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import json

app = Flask(__name__)
CORS(app)

# In-memory storage for demo
admins = [
    {
        'id': 1,
        'username': 'admin',
        'password': 'admin123',
        'email': 'yadavabhinav551@gmail.com',
        'phone': '9876543210',
        'bankDetails': None,
        'upiDetails': None
    }
]

customers = []
orders = []
products = []
payment_details = {
    'bank': None,
    'upi': None
}
payment_proofs = []
password_reset_tokens = {}  # For forgot password feature

# Admin Login
@app.route('/api/admin/login', methods=['POST'])
def admin_login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'success': False, 'message': 'Username and password are required'}), 400

    admin = next((a for a in admins if a['username'] == username and a['password'] == password), None)

    if admin:
        token = f"{username}:{datetime.now().timestamp()}"
        return jsonify({
            'success': True,
            'message': 'Login successful',
            'token': token,
            'admin': {
                'id': admin['id'],
                'username': admin['username'],
                'email': admin['email']
            }
        }), 200
    else:
        return jsonify({'success': False, 'message': 'Invalid username or password'}), 401

# Customer Login
@app.route('/api/customer/login', methods=['POST'])
def customer_login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'success': False, 'message': 'Email and password are required'}), 400

    customer = next((c for c in customers if c['email'] == email and c['password'] == password), None)

    if customer:
        token = f"{email}:{datetime.now().timestamp()}"
        return jsonify({
            'success': True,
            'message': 'Login successful',
            'token': token,
            'customer': {
                'id': customer['id'],
                'name': customer['name'],
                'email': customer['email']
            }
        }), 200
    else:
        return jsonify({'success': False, 'message': 'Invalid email or password'}), 401

# Customer Register
@app.route('/api/customer/register', methods=['POST'])
def customer_register():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    phone = data.get('phone')

    if not name or not email or not password or not phone:
        return jsonify({'success': False, 'message': 'All fields are required'}), 400

    if any(c['email'] == email for c in customers):
        return jsonify({'success': False, 'message': 'Email already registered'}), 400

    new_customer = {
        'id': len(customers) + 1,
        'name': name,
        'email': email,
        'password': password,
        'phone': phone,
        'createdAt': datetime.now().isoformat()
    }

    customers.append(new_customer)
    token = f"{email}:{datetime.now().timestamp()}"

    return jsonify({
        'success': True,
        'message': 'Registration successful',
        'token': token,
        'customer': {
            'id': new_customer['id'],
            'name': new_customer['name'],
            'email': new_customer['email']
        }
    }), 201

# Get Admin Stats
@app.route('/api/admin/stats', methods=['GET'])
def get_stats():
    total_revenue = sum(order.get('total', 0) for order in orders)
    return jsonify({
        'success': True,
        'stats': {
            'totalOrders': len(orders),
            'totalRevenue': total_revenue,
            'totalCustomers': len(customers),
            'totalProducts': len(products)
        }
    }), 200

# Get All Orders
@app.route('/api/admin/orders', methods=['GET'])
def get_orders():
    return jsonify({'success': True, 'orders': orders}), 200

# Get All Products
@app.route('/api/admin/products', methods=['GET'])
def get_products():
    return jsonify({'success': True, 'products': products}), 200

# Get All Customers
@app.route('/api/admin/customers', methods=['GET'])
def get_customers():
    return jsonify({'success': True, 'customers': customers}), 200

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

# Add Product
@app.route('/api/admin/products', methods=['POST'])
def add_product():
    data = request.get_json()
    brand = data.get('brand')
    model = data.get('model')
    price = data.get('price')

    if not brand or not model or price is None:
        return jsonify({'success': False, 'message': 'Brand, model, and price are required'}), 400

    new_product = {
        'id': len(products) + 1,
        'brand': brand,
        'model': model,
        'price': price,
        'specs': data.get('specs', {}),
        'condition': data.get('condition', 'good'),
        'warranty': data.get('warranty', '6 months'),
        'createdAt': datetime.now().isoformat()
    }

    products.append(new_product)

    return jsonify({
        'success': True,
        'message': 'Product added successfully',
        'product': new_product
    }), 201

# Update Product
@app.route('/api/admin/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)

    if not product:
        return jsonify({'success': False, 'message': 'Product not found'}), 404

    data = request.get_json()
    product.update(data)

    return jsonify({
        'success': True,
        'message': 'Product updated successfully',
        'product': product
    }), 200

# Delete Product
@app.route('/api/admin/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    global products
    product_index = next((i for i, p in enumerate(products) if p['id'] == product_id), None)

    if product_index is None:
        return jsonify({'success': False, 'message': 'Product not found'}), 404

    deleted_product = products.pop(product_index)

    return jsonify({
        'success': True,
        'message': 'Product deleted successfully',
        'product': deleted_product
    }), 200

# Change Admin Password
@app.route('/api/admin/change-password', methods=['POST'])
def change_password():
    data = request.get_json()
    username = data.get('username')
    old_password = data.get('oldPassword')
    new_password = data.get('newPassword')

    if not username or not old_password or not new_password:
        return jsonify({'success': False, 'message': 'All fields are required'}), 400

    admin = next((a for a in admins if a['username'] == username and a['password'] == old_password), None)

    if not admin:
        return jsonify({'success': False, 'message': 'Invalid username or old password'}), 401

    admin['password'] = new_password

    return jsonify({'success': True, 'message': 'Password changed successfully'}), 200

# Forgot Password - Request Reset
@app.route('/api/admin/forgot-password', methods=['POST'])
def forgot_password():
    data = request.get_json()
    email = data.get('email')
    
    if not email:
        return jsonify({'success': False, 'message': 'Email is required'}), 400
    
    admin = next((a for a in admins if a['email'] == email), None)
    
    if not admin:
        return jsonify({'success': False, 'message': 'Email not found in system'}), 404
    
    # Generate reset code (in real app, send via email)
    import random
    import string
    reset_code = ''.join(random.choices(string.digits, k=6))
    
    password_reset_tokens[email] = {
        'code': reset_code,
        'timestamp': datetime.now().isoformat(),
        'attempts': 0
    }
    
    return jsonify({
        'success': True, 
        'message': f'Reset code sent to {email}',
        'resetCode': reset_code  # In demo, showing code. In production, send via email only
    }), 200

# Forgot Password - Reset Password
@app.route('/api/admin/reset-password', methods=['POST'])
def reset_password():
    data = request.get_json()
    email = data.get('email')
    reset_code = data.get('resetCode')
    new_password = data.get('newPassword')
    
    if not email or not reset_code or not new_password:
        return jsonify({'success': False, 'message': 'All fields are required'}), 400
    
    if email not in password_reset_tokens:
        return jsonify({'success': False, 'message': 'Password reset request not found. Request again.'}), 404
    
    token_data = password_reset_tokens[email]
    
    if token_data['code'] != reset_code:
        token_data['attempts'] += 1
        if token_data['attempts'] >= 3:
            del password_reset_tokens[email]
            return jsonify({'success': False, 'message': 'Too many failed attempts. Request password reset again.'}), 403
        return jsonify({'success': False, 'message': 'Invalid reset code'}), 401
    
    admin = next((a for a in admins if a['email'] == email), None)
    
    if not admin:
        return jsonify({'success': False, 'message': 'Admin not found'}), 404
    
    admin['password'] = new_password
    del password_reset_tokens[email]
    
    return jsonify({'success': True, 'message': 'Password reset successfully'}), 200

# Get Payment Details (for customers)
@app.route('/api/payment-details', methods=['GET'])
def get_payment_details():
    return jsonify({
        'success': True,
        'paymentDetails': payment_details
    }), 200

# Add/Update Bank Details (Admin)
@app.route('/api/admin/payment-details/bank', methods=['POST'])
def add_bank_details():
    data = request.get_json()
    bank_name = data.get('bankName')
    account_holder = data.get('accountHolder')
    account_number = data.get('accountNumber')
    ifsc_code = data.get('ifscCode')

    if not all([bank_name, account_holder, account_number, ifsc_code]):
        return jsonify({'success': False, 'message': 'All fields are required'}), 400

    payment_details['bank'] = {
        'bankName': bank_name,
        'accountHolder': account_holder,
        'accountNumber': account_number[-4:],  # Show only last 4 digits
        'ifscCode': ifsc_code,
        'fullAccountNumber': account_number,  # Keep full number for verification only
        'createdAt': datetime.now().isoformat()
    }

    return jsonify({
        'success': True,
        'message': 'Bank details saved successfully',
        'bankDetails': payment_details['bank']
    }), 200

# Add/Update UPI Details (Admin)
@app.route('/api/admin/payment-details/upi', methods=['POST'])
def add_upi_details():
    data = request.get_json()
    upi_id = data.get('upiId')
    owner_name = data.get('ownerName')

    if not upi_id or not owner_name:
        return jsonify({'success': False, 'message': 'UPI ID and Owner Name are required'}), 400

    payment_details['upi'] = {
        'upiId': upi_id,
        'ownerName': owner_name,
        'createdAt': datetime.now().isoformat()
    }

    return jsonify({
        'success': True,
        'message': 'UPI details saved successfully',
        'upiDetails': payment_details['upi']
    }), 200

# Create Order with Payment Details
@app.route('/api/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    
    required_fields = ['customerName', 'customerEmail', 'customerPhone', 'items', 'shippingAddress', 'paymentMethod']
    if not all(field in data for field in required_fields):
        return jsonify({'success': False, 'message': 'Missing required fields'}), 400

    new_order = {
        'id': len(orders) + 1,
        'orderId': 'ORDER-' + str(datetime.now().timestamp()).replace('.', ''),
        'customerName': data.get('customerName'),
        'customerEmail': data.get('customerEmail'),
        'customerPhone': data.get('customerPhone'),
        'items': data.get('items'),
        'total': data.get('total'),
        'paymentMethod': data.get('paymentMethod'),
        'shippingAddress': data.get('shippingAddress'),
        'status': 'pending',  # pending, payment_pending, payment_verified, completed
        'paymentProof': None,
        'transactionId': None,
        'createdAt': datetime.now().isoformat(),
        'updatedAt': datetime.now().isoformat()
    }

    orders.append(new_order)

    return jsonify({
        'success': True,
        'message': 'Order created successfully',
        'order': new_order
    }), 201

# Submit Payment Proof
@app.route('/api/orders/<int:order_id>/payment-proof', methods=['POST'])
def submit_payment_proof(order_id):
    order = next((o for o in orders if o['id'] == order_id), None)
    
    if not order:
        return jsonify({'success': False, 'message': 'Order not found'}), 404

    data = request.get_json()
    transaction_id = data.get('transactionId')
    proof_description = data.get('proofDescription')

    if not transaction_id or not proof_description:
        return jsonify({'success': False, 'message': 'Transaction ID and proof are required'}), 400

    proof_record = {
        'orderId': order_id,
        'transactionId': transaction_id,
        'proofDescription': proof_description,
        'uploadedAt': datetime.now().isoformat(),
        'status': 'pending'  # pending, verified, rejected
    }

    payment_proofs.append(proof_record)
    order['transactionId'] = transaction_id
    order['paymentProof'] = proof_record
    order['status'] = 'payment_pending'
    order['updatedAt'] = datetime.now().isoformat()

    return jsonify({
        'success': True,
        'message': 'Payment proof submitted successfully',
        'proof': proof_record
    }), 201

# Get Orders with Payment Status (Admin)
@app.route('/api/admin/orders-with-payment', methods=['GET'])
def get_orders_with_payment():
    orders_data = []
    for order in orders:
        order_data = order.copy()
        if order.get('paymentProof'):
            order_data['paymentProofStatus'] = order['paymentProof'].get('status')
        orders_data.append(order_data)
    
    return jsonify({'success': True, 'orders': orders_data}), 200

# Verify and Confirm Payment (Admin)
@app.route('/api/admin/orders/<int:order_id>/verify-payment', methods=['POST'])
def verify_payment(order_id):
    order = next((o for o in orders if o['id'] == order_id), None)
    
    if not order:
        return jsonify({'success': False, 'message': 'Order not found'}), 404

    data = request.get_json()
    action = data.get('action')  # 'approve' or 'reject'
    notes = data.get('notes', '')

    if action not in ['approve', 'reject']:
        return jsonify({'success': False, 'message': 'Invalid action'}), 400

    if order.get('paymentProof'):
        if action == 'approve':
            order['paymentProof']['status'] = 'verified'
            order['status'] = 'completed'
            message = 'Payment verified successfully'
        else:
            order['paymentProof']['status'] = 'rejected'
            order['status'] = 'payment_pending'
            message = 'Payment rejected'
        
        if notes:
            order['paymentProof']['adminNotes'] = notes
        
        order['paymentProof']['verifiedAt'] = datetime.now().isoformat()
        order['updatedAt'] = datetime.now().isoformat()

        return jsonify({
            'success': True,
            'message': message,
            'order': order
        }), 200
    else:
        return jsonify({'success': False, 'message': 'No payment proof found for this order'}), 404

# Get Pending Payment Verifications (Admin)
@app.route('/api/admin/pending-verifications', methods=['GET'])
def get_pending_verifications():
    pending_orders = [o for o in orders if o.get('status') == 'payment_pending']
    return jsonify({'success': True, 'orders': pending_orders}), 200

# Health Check
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'success': True,
        'message': 'Server is running',
        'timestamp': datetime.now().isoformat()
    }), 200

if __name__ == '__main__':
    print("✅ Backend Server is running on http://localhost:5000")
    print("🔐 Admin credentials: username: admin, password: admin123")
    print("📊 API endpoints available at http://localhost:5000/api")
    app.run(debug=True, port=5000)
