from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import os
import secrets
import validators
from functools import wraps
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

app = Flask(__name__)

# ===== DATABASE CONFIGURATION =====
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///laptop_shop.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ===== EMAIL CONFIGURATION =====
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', True)
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME', '')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD', '')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER', 'noreply@secondhandpcstudio.com')

# ===== SECURITY CONFIGURATION =====
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key-change-in-production')

db = SQLAlchemy(app)
mail = Mail(app)
CORS(app)

# ===== DATABASE MODELS =====

class Admin(db.Model):
    __tablename__ = 'admins'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    bank_details = db.Column(db.JSON)
    upi_details = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'phone': self.phone
        }


class Customer(db.Model):
    __tablename__ = 'customers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    otp = db.Column(db.String(6))
    otp_expires = db.Column(db.DateTime)
    is_verified = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    orders = db.relationship('Order', backref='customer', lazy=True, cascade='all, delete-orphan')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def generate_otp(self):
        self.otp = str(secrets.randbelow(1000000)).zfill(6)
        self.otp_expires = datetime.utcnow() + timedelta(minutes=10)
        db.session.commit()
        return self.otp
    
    def verify_otp(self, otp):
        if self.otp == otp and self.otp_expires > datetime.utcnow():
            self.otp = None
            self.otp_expires = None
            self.is_verified = True
            db.session.commit()
            return True
        return False
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'is_verified': self.is_verified
        }


class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(120), nullable=False)
    processor = db.Column(db.String(120))
    ram = db.Column(db.String(50))
    storage = db.Column(db.String(50))
    condition = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Float, nullable=False)
    original_price = db.Column(db.Float)
    warranty = db.Column(db.String(50))
    rating = db.Column(db.Float, default=0)
    reviews_count = db.Column(db.Integer, default=0)
    stock = db.Column(db.Integer, default=1)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    orders = db.relationship('OrderItem', backref='product', lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'brand': self.brand,
            'model': self.model,
            'specs': {
                'processor': self.processor,
                'ram': self.ram,
                'storage': self.storage
            },
            'condition': self.condition,
            'price': self.price,
            'originalPrice': self.original_price,
            'warranty': self.warranty,
            'rating': self.rating,
            'reviews': self.reviews_count,
            'stock': self.stock
        }


class Order(db.Model):
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    order_number = db.Column(db.String(20), unique=True, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    gst = db.Column(db.Float, default=0)
    final_price = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.String(50))
    status = db.Column(db.String(20), default='pending')
    shipping_address = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    items = db.relationship('OrderItem', backref='order', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'order_number': self.order_number,
            'customer_id': self.customer_id,
            'total_price': self.total_price,
            'gst': self.gst,
            'final_price': self.final_price,
            'payment_method': self.payment_method,
            'status': self.status,
            'created_at': self.created_at.isoformat(),
            'items': [item.to_dict() for item in self.items]
        }


class OrderItem(db.Model):
    __tablename__ = 'order_items'
    
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, default=1)
    price = db.Column(db.Float)
    
    def to_dict(self):
        return {
            'id': self.id,
            'product': self.product.to_dict(),
            'quantity': self.quantity,
            'price': self.price
        }


class PasswordResetToken(db.Model):
    __tablename__ = 'password_reset_tokens'
    
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    token = db.Column(db.String(255), unique=True, nullable=False)
    expires_at = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    customer = db.relationship('Customer')


# ===== HELPER FUNCTIONS =====

def send_otp_email(email, otp):
    """Send OTP via email"""
    try:
        msg = Message(
            subject='Your OTP for Second Hand PC Studio',
            recipients=[email],
            html=f'''
            <h2>Welcome to Second Hand PC Studio</h2>
            <p>Your OTP is: <strong>{otp}</strong></p>
            <p>This OTP will expire in 10 minutes.</p>
            <p>Do not share this OTP with anyone.</p>
            '''
        )
        mail.send(msg)
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False


def send_order_confirmation(customer_email, order):
    """Send order confirmation email"""
    try:
        msg = Message(
            subject=f'Order Confirmation - {order.order_number}',
            recipients=[customer_email],
            html=f'''
            <h2>Order Confirmed!</h2>
            <p>Your order <strong>{order.order_number}</strong> has been received.</p>
            <p><strong>Order Details:</strong></p>
            <ul>
                <li>Items: {len(order.items)}</li>
                <li>Total: ₹{order.final_price}</li>
                <li>Payment Method: {order.payment_method}</li>
            </ul>
            <p>We will notify you when your order is shipped.</p>
            '''
        )
        mail.send(msg)
        return True
    except Exception as e:
        print(f"Error sending confirmation: {e}")
        return False


def send_password_reset_email(email, reset_token):
    """Send password reset link via email"""
    try:
        reset_link = f"http://localhost:5500/reset-password.html?token={reset_token}"
        msg = Message(
            subject='Password Reset - Second Hand PC Studio',
            recipients=[email],
            html=f'''
            <h2>Password Reset Request</h2>
            <p>Click the link below to reset your password:</p>
            <a href="{reset_link}">Reset Password</a>
            <p>This link will expire in 1 hour.</p>
            <p>If you didn't request this, please ignore this email.</p>
            '''
        )
        mail.send(msg)
        return True
    except Exception as e:
        print(f"Error sending reset email: {e}")
        return False


def validate_email(email):
    """Validate email format"""
    return validators.email(email) is not None


def validate_phone(phone):
    """Validate phone number"""
    phone_digits = ''.join(filter(str.isdigit, phone))
    return len(phone_digits) >= 10


def token_required(f):
    """Decorator to check authentication token"""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization', '').replace('Bearer ', '')
        if not token:
            return jsonify({'success': False, 'message': 'Token required'}), 401
        return f(*args, **kwargs)
    return decorated


# ===== API ENDPOINTS =====

# ===== ADMIN ENDPOINTS =====

@app.route('/api/admin/login', methods=['POST'])
def admin_login():
    """Admin login with credentials"""
    try:
        data = request.get_json()
        username = data.get('username', '').strip()
        password = data.get('password', '')
        
        if not username or not password:
            return jsonify({'success': False, 'message': 'Username and password required'}), 400
        
        admin = Admin.query.filter_by(username=username).first()
        
        if admin and admin.check_password(password):
            token = secrets.token_urlsafe(32)
            return jsonify({
                'success': True,
                'message': 'Login successful',
                'token': token,
                'admin': admin.to_dict()
            }), 200
        else:
            return jsonify({'success': False, 'message': 'Invalid credentials'}), 401
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500


# ===== CUSTOMER ENDPOINTS =====

@app.route('/api/customer/register', methods=['POST'])
def customer_register():
    """Register new customer"""
    try:
        data = request.get_json()
        name = data.get('name', '').strip()
        email = data.get('email', '').strip().lower()
        phone = data.get('phone', '').strip()
        password = data.get('password', '')
        
        # Validation
        if not all([name, email, phone, password]):
            return jsonify({'success': False, 'message': 'All fields required'}), 400
        
        if len(password) < 6:
            return jsonify({'success': False, 'message': 'Password must be at least 6 characters'}), 400
        
        if not validate_email(email):
            return jsonify({'success': False, 'message': 'Invalid email format'}), 400
        
        if not validate_phone(phone):
            return jsonify({'success': False, 'message': 'Invalid phone number'}), 400
        
        if Customer.query.filter_by(email=email).first():
            return jsonify({'success': False, 'message': 'Email already registered'}), 400
        
        # Create customer
        customer = Customer(name=name, email=email, phone=phone)
        customer.set_password(password)
        
        db.session.add(customer)
        db.session.commit()
        
        # Send OTP
        otp = customer.generate_otp()
        send_otp_email(email, otp)
        
        return jsonify({
            'success': True,
            'message': 'Registration successful. OTP sent to email.',
            'customer_id': customer.id
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500


@app.route('/api/customer/login', methods=['POST'])
def customer_login():
    """Customer login"""
    try:
        data = request.get_json()
        email = data.get('email', '').strip().lower()
        password = data.get('password', '')
        
        if not email or not password:
            return jsonify({'success': False, 'message': 'Email and password required'}), 400
        
        customer = Customer.query.filter_by(email=email).first()
        
        if customer and customer.check_password(password):
            token = secrets.token_urlsafe(32)
            return jsonify({
                'success': True,
                'message': 'Login successful',
                'token': token,
                'customer': customer.to_dict()
            }), 200
        else:
            return jsonify({'success': False, 'message': 'Invalid credentials'}), 401
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500


@app.route('/api/customer/verify-otp', methods=['POST'])
def verify_otp():
    """Verify OTP"""
    try:
        data = request.get_json()
        customer_id = data.get('customer_id')
        otp = data.get('otp', '').strip()
        
        if not customer_id or not otp:
            return jsonify({'success': False, 'message': 'Customer ID and OTP required'}), 400
        
        customer = Customer.query.get(customer_id)
        
        if not customer:
            return jsonify({'success': False, 'message': 'Customer not found'}), 404
        
        if customer.verify_otp(otp):
            return jsonify({
                'success': True,
                'message': 'OTP verified successfully',
                'customer': customer.to_dict()
            }), 200
        else:
            return jsonify({'success': False, 'message': 'Invalid or expired OTP'}), 401
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500


@app.route('/api/customer/forgot-password', methods=['POST'])
def forgot_password():
    """Initiate password reset"""
    try:
        data = request.get_json()
        email = data.get('email', '').strip().lower()
        
        if not email:
            return jsonify({'success': False, 'message': 'Email required'}), 400
        
        customer = Customer.query.filter_by(email=email).first()
        
        if customer:
            # Generate reset token
            token = secrets.token_urlsafe(32)
            reset = PasswordResetToken(
                customer_id=customer.id,
                token=token,
                expires_at=datetime.utcnow() + timedelta(hours=1)
            )
            db.session.add(reset)
            db.session.commit()
            
            # Send email
            send_password_reset_email(email, token)
        
        # Always return success for security
        return jsonify({
            'success': True,
            'message': 'If email exists, reset link sent'
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500


@app.route('/api/customer/reset-password', methods=['POST'])
def reset_password():
    """Reset password with token"""
    try:
        data = request.get_json()
        token = data.get('token', '').strip()
        new_password = data.get('password', '')
        
        if not token or not new_password:
            return jsonify({'success': False, 'message': 'Token and password required'}), 400
        
        if len(new_password) < 6:
            return jsonify({'success': False, 'message': 'Password must be at least 6 characters'}), 400
        
        reset_token = PasswordResetToken.query.filter_by(token=token).first()
        
        if not reset_token or reset_token.expires_at < datetime.utcnow():
            return jsonify({'success': False, 'message': 'Invalid or expired token'}), 401
        
        customer = reset_token.customer
        customer.set_password(new_password)
        db.session.delete(reset_token)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Password reset successful'
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500


# ===== PRODUCT ENDPOINTS =====

@app.route('/api/products', methods=['GET'])
def get_products():
    """Get all products"""
    try:
        products = Product.query.all()
        return jsonify({
            'success': True,
            'products': [p.to_dict() for p in products]
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500


@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Get single product"""
    try:
        product = Product.query.get(product_id)
        if not product:
            return jsonify({'success': False, 'message': 'Product not found'}), 404
        return jsonify({
            'success': True,
            'product': product.to_dict()
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500


@app.route('/api/admin/products', methods=['POST'])
@token_required
def create_product():
    """Create new product (Admin only)"""
    try:
        data = request.get_json()
        
        product = Product(
            brand=data.get('brand'),
            model=data.get('model'),
            processor=data.get('processor'),
            ram=data.get('ram'),
            storage=data.get('storage'),
            condition=data.get('condition'),
            price=data.get('price'),
            original_price=data.get('originalPrice'),
            warranty=data.get('warranty'),
            stock=data.get('stock', 1)
        )
        
        db.session.add(product)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Product created',
            'product': product.to_dict()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500


# ===== ORDER ENDPOINTS =====

@app.route('/api/orders', methods=['POST'])
@token_required
def create_order():
    """Create new order"""
    try:
        data = request.get_json()
        customer_id = data.get('customer_id')
        items = data.get('items', [])
        payment_method = data.get('payment_method')
        shipping_address = data.get('shipping_address')
        
        if not items:
            return jsonify({'success': False, 'message': 'Cart is empty'}), 400
        
        customer = Customer.query.get(customer_id)
        if not customer:
            return jsonify({'success': False, 'message': 'Customer not found'}), 404
        
        # Calculate total
        total_price = 0
        order_items = []
        
        for item in items:
            product = Product.query.get(item['product_id'])
            if not product:
                return jsonify({'success': False, 'message': f'Product {item["product_id"]} not found'}), 404
            
            if product.stock < item['quantity']:
                return jsonify({'success': False, 'message': f'Insufficient stock for {product.model}'}), 400
            
            item_price = product.price * item['quantity']
            total_price += item_price
            
            order_item = OrderItem(
                product_id=product.id,
                quantity=item['quantity'],
                price=item_price
            )
            order_items.append(order_item)
            product.stock -= item['quantity']
        
        # Calculate GST (18%)
        gst = total_price * 0.18
        final_price = total_price + gst
        
        # Create order
        order_number = f"ORD-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}"
        order = Order(
            order_number=order_number,
            customer_id=customer_id,
            total_price=total_price,
            gst=gst,
            final_price=final_price,
            payment_method=payment_method,
            status='pending',
            shipping_address=shipping_address
        )
        
        order.items = order_items
        db.session.add(order)
        db.session.commit()
        
        # Send confirmation email
        send_order_confirmation(customer.email, order)
        
        return jsonify({
            'success': True,
            'message': 'Order created successfully',
            'order': order.to_dict()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500


@app.route('/api/orders/<int:order_id>', methods=['GET'])
@token_required
def get_order(order_id):
    """Get order details"""
    try:
        order = Order.query.get(order_id)
        if not order:
            return jsonify({'success': False, 'message': 'Order not found'}), 404
        return jsonify({
            'success': True,
            'order': order.to_dict()
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500


# ===== DATABASE INITIALIZATION =====

@app.route('/api/init-db', methods=['POST'])
def init_database():
    """Initialize database with sample data"""
    try:
        db.create_all()
        
        # Check if data exists
        if Admin.query.first():
            return jsonify({'success': False, 'message': 'Database already initialized'}), 400
        
        # Create admin
        admin = Admin(
            username='admin',
            email='admin@secondhandpcstudio.com',
            phone='9876543210'
        )
        admin.set_password('admin123')
        
        # Sample products
        products_data = [
            {
                'brand': 'Dell',
                'model': 'Latitude 5420',
                'processor': 'Intel i5-11th Gen',
                'ram': '8GB DDR4',
                'storage': '512GB SSD',
                'condition': 'excellent',
                'price': 35000,
                'original_price': 45000,
                'warranty': '12 months',
                'stock': 5
            },
            {
                'brand': 'HP',
                'model': 'EliteBook 840 G8',
                'processor': 'Intel i7-11th Gen',
                'ram': '16GB DDR4',
                'storage': '512GB SSD',
                'condition': 'excellent',
                'price': 45000,
                'original_price': 58000,
                'warranty': '12 months',
                'stock': 3
            },
            {
                'brand': 'Lenovo',
                'model': 'ThinkPad E15',
                'processor': 'Ryzen 5 5600H',
                'ram': '8GB DDR4',
                'storage': '256GB SSD',
                'condition': 'good',
                'price': 28000,
                'original_price': 38000,
                'warranty': '6 months',
                'stock': 4
            },
            {
                'brand': 'ASUS',
                'model': 'VivoBook 15',
                'processor': 'AMD Ryzen 7',
                'ram': '16GB DDR4',
                'storage': '512GB SSD',
                'condition': 'good',
                'price': 42000,
                'original_price': 55000,
                'warranty': '12 months',
                'stock': 2
            },
            {
                'brand': 'Dell',
                'model': 'XPS 13',
                'processor': 'Intel i7-1185G7',
                'ram': '16GB DDR4',
                'storage': '512GB SSD',
                'condition': 'excellent',
                'price': 65000,
                'original_price': 85000,
                'warranty': '12 months',
                'stock': 1
            },
            {
                'brand': 'HP',
                'model': 'Pavilion 15',
                'processor': 'Intel i5-11th Gen',
                'ram': '8GB DDR4',
                'storage': '256GB SSD',
                'condition': 'fair',
                'price': 22000,
                'original_price': 32000,
                'warranty': '6 months',
                'stock': 6
            }
        ]
        
        db.session.add(admin)
        
        for prod in products_data:
            product = Product(**prod)
            db.session.add(product)
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Database initialized with sample data'
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'success': True,
        'message': 'Server is running',
        'timestamp': datetime.utcnow().isoformat()
    }), 200


@app.errorhandler(404)
def not_found(e):
    return jsonify({'success': False, 'message': 'Endpoint not found'}), 404


@app.errorhandler(500)
def internal_error(e):
    db.session.rollback()
    return jsonify({'success': False, 'message': 'Internal server error'}), 500


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    # Development: debug=True, localhost
    # Production: debug=False, 0.0.0.0
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_PORT', 5000))
    app.run(debug=debug_mode, host=host, port=port)
