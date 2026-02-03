// API Configuration - Supports both localhost and deployed environments
let API_URL;

// Detect environment and set API URL
if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
    // Development environment
    API_URL = 'http://localhost:5000/api';
} else if (window.location.hostname.includes('vercel.app')) {
    // Frontend hosted on Vercel - use the Render backend URL (actual service name)
    API_URL = 'https://pcstudio-abhi-1.onrender.com/api';
} else {
    // Fallback: try the Render domain (common case for direct visits)
    API_URL = 'https://pcstudio-abhi-1.onrender.com/api';
}

// Sample Products Data
const productsData = [
    {
        id: 1,
        brand: 'Dell',
        model: 'Latitude 5420',
        image: '💻',
        specs: {
            processor: 'Intel i5-11th Gen',
            ram: '8GB DDR4',
            storage: '512GB SSD'
        },
        condition: 'excellent',
        price: 35000,
        originalPrice: 45000,
        warranty: '12 months',
        rating: 4.5,
        reviews: 24
    },
    {
        id: 2,
        brand: 'HP',
        model: 'EliteBook 840 G8',
        image: '💻',
        specs: {
            processor: 'Intel i7-11th Gen',
            ram: '16GB DDR4',
            storage: '512GB SSD'
        },
        condition: 'excellent',
        price: 45000,
        originalPrice: 58000,
        warranty: '12 months',
        rating: 4.7,
        reviews: 32
    },
    {
        id: 3,
        brand: 'Lenovo',
        model: 'ThinkPad E15',
        image: '💻',
        specs: {
            processor: 'Ryzen 5 5600H',
            ram: '8GB DDR4',
            storage: '256GB SSD'
        },
        condition: 'good',
        price: 28000,
        originalPrice: 38000,
        warranty: '6 months',
        rating: 4.3,
        reviews: 18
    },
    {
        id: 4,
        brand: 'ASUS',
        model: 'VivoBook 15',
        image: '💻',
        specs: {
            processor: 'AMD Ryzen 7',
            ram: '16GB DDR4',
            storage: '512GB SSD'
        },
        condition: 'good',
        price: 42000,
        originalPrice: 55000,
        warranty: '12 months',
        rating: 4.4,
        reviews: 28
    },
    {
        id: 5,
        brand: 'Dell',
        model: 'XPS 13',
        image: '💻',
        specs: {
            processor: 'Intel i7-1185G7',
            ram: '16GB DDR4',
            storage: '512GB SSD'
        },
        condition: 'excellent',
        price: 65000,
        originalPrice: 85000,
        warranty: '12 months',
        rating: 4.8,
        reviews: 45
    },
    {
        id: 6,
        brand: 'HP',
        model: 'Pavilion 15',
        image: '💻',
        specs: {
            processor: 'Intel i5-11th Gen',
            ram: '8GB DDR4',
            storage: '256GB SSD'
        },
        condition: 'fair',
        price: 22000,
        originalPrice: 32000,
        warranty: '6 months',
        rating: 4.0,
        reviews: 15
    }
];

// Sample Reviews Data
const reviewsData = [
    {
        id: 1,
        reviewer: 'Rajesh Kumar',
        rating: 5,
        text: 'Excellent quality laptop! Received exactly as described. Highly recommended!',
        product: 'Dell Latitude 5420',
        date: '2025-01-15'
    },
    {
        id: 2,
        reviewer: 'Priya Singh',
        rating: 4,
        text: 'Good value for money. Works perfectly without any issues.',
        product: 'HP EliteBook 840 G8',
        date: '2025-01-10'
    },
    {
        id: 3,
        reviewer: 'Amit Patel',
        rating: 5,
        text: 'Outstanding product quality and fast shipping. Great customer service!',
        product: 'Lenovo ThinkPad E15',
        date: '2025-01-05'
    },
    {
        id: 4,
        reviewer: 'Neha Sharma',
        rating: 4,
        text: 'Great laptop for the price. Battery life is excellent.',
        product: 'ASUS VivoBook 15',
        date: '2024-12-28'
    },
    {
        id: 5,
        reviewer: 'Vikram Desai',
        rating: 5,
        text: 'Premium quality! The laptop is in perfect condition. Very happy with my purchase.',
        product: 'Dell XPS 13',
        date: '2024-12-20'
    },
    {
        id: 6,
        reviewer: 'Anjali Gupta',
        rating: 4,
        text: 'Good product, though could have included more accessories. Overall satisfied.',
        product: 'HP Pavilion 15',
        date: '2024-12-15'
    }
];

// DOM Elements
const navToggle = document.getElementById('navToggle');
const navMenu = document.getElementById('navMenu');
const productsGrid = document.getElementById('productsGrid');
const reviewsGrid = document.getElementById('reviewsGrid');
const searchInput = document.getElementById('searchInput');
const brandFilter = document.getElementById('brandFilter');
const priceFilter = document.getElementById('priceFilter');
const authModal = document.getElementById('authModal');
const cartModal = document.getElementById('cartModal');
const cartCount = document.getElementById('cartCount');

// Initialize App
document.addEventListener('DOMContentLoaded', function() {
    renderProducts(productsData);
    renderReviews(reviewsData);
    updateCartCount();
    setupEventListeners();
});

// Setup Event Listeners
function setupEventListeners() {
    // Mobile Menu Toggle
    if (navToggle) {
        navToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
        });
    }

    // Close mobile menu when clicking on a link
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', function() {
            navMenu.classList.remove('active');
        });
    });

    // Search and Filter
    if (searchInput) searchInput.addEventListener('input', filterProducts);
    if (brandFilter) brandFilter.addEventListener('change', filterProducts);
    if (priceFilter) priceFilter.addEventListener('change', filterProducts);

    // Close modals when clicking outside
    window.addEventListener('click', function(event) {
        if (event.target === authModal) closeAuthModal();
        if (event.target === cartModal) closeCart();
    });
}

// Render Products
function renderProducts(products) {
    if (!productsGrid) return;
    
    productsGrid.innerHTML = '';
    
    if (products.length === 0) {
        productsGrid.innerHTML = '<p style="grid-column: 1/-1; text-align: center; padding: 2rem; color: #7f8c8d;">No products found. Try adjusting your filters.</p>';
        return;
    }

    products.forEach(product => {
        const discount = Math.round(((product.originalPrice - product.price) / product.originalPrice) * 100);
        const conditionClass = `condition-${product.condition}`;
        const conditionText = product.condition.charAt(0).toUpperCase() + product.condition.slice(1);

        const productCard = document.createElement('div');
        productCard.className = 'product-card';
        productCard.innerHTML = `
            <div class="product-image">
                ${product.image}
                <span class="product-badge">${discount}% OFF</span>
            </div>
            <div class="product-info">
                <h3 class="product-title">${product.brand} ${product.model}</h3>
                <div class="product-specs">
                    <div class="product-spec">
                        <span>Processor:</span>
                        <span>${product.specs.processor}</span>
                    </div>
                    <div class="product-spec">
                        <span>RAM:</span>
                        <span>${product.specs.ram}</span>
                    </div>
                    <div class="product-spec">
                        <span>Storage:</span>
                        <span>${product.specs.storage}</span>
                    </div>
                </div>
                <span class="product-condition ${conditionClass}">${conditionText}</span>
                <div class="product-rating">
                    <i class="fas fa-star"></i> ${product.rating}/5 (${product.reviews} reviews)
                </div>
                <div class="product-price">
                    <div class="price-display">
                        <span class="current-price">₹${product.price.toLocaleString()}</span>
                        <span class="original-price">₹${product.originalPrice.toLocaleString()}</span>
                    </div>
                    <button class="add-to-cart-btn" onclick="addToCart(${product.id}, '${product.brand} ${product.model}', ${product.price})">
                        <i class="fas fa-shopping-cart"></i>
                    </button>
                </div>
                <button class="btn btn-outline" style="width: 100%; margin-top: 0.5rem;" onclick="viewProductDetails(${product.id})">
                    View Details
                </button>
            </div>
        `;
        productsGrid.appendChild(productCard);
    });
}

// Render Reviews
function renderReviews(reviews) {
    if (!reviewsGrid) return;
    
    reviewsGrid.innerHTML = '';
    reviews.slice(0, 6).forEach(review => {
        const stars = '⭐'.repeat(review.rating);
        const reviewCard = document.createElement('div');
        reviewCard.className = 'review-card';
        reviewCard.innerHTML = `
            <div class="review-header">
                <div class="reviewer-name">${review.reviewer}</div>
                <div class="review-stars">${stars}</div>
            </div>
            <p class="review-text">"${review.text}"</p>
            <div class="review-product">Reviewed: ${review.product}</div>
            <div class="review-date">${new Date(review.date).toLocaleDateString('en-IN')}</div>
        `;
        reviewsGrid.appendChild(reviewCard);
    });
}

// Filter Products
function filterProducts() {
    const searchTerm = searchInput?.value?.toLowerCase() || '';
    const selectedBrand = brandFilter?.value || '';
    const priceRange = priceFilter?.value || '';

    let filtered = productsData.filter(product => {
        // Search filter
        const matchesSearch = product.brand.toLowerCase().includes(searchTerm) ||
                            product.model.toLowerCase().includes(searchTerm);
        
        // Brand filter
        const matchesBrand = !selectedBrand || product.brand === selectedBrand;
        
        // Price filter
        let matchesPrice = true;
        if (priceRange === '0-20000') matchesPrice = product.price <= 20000;
        else if (priceRange === '20000-40000') matchesPrice = product.price >= 20000 && product.price <= 40000;
        else if (priceRange === '40000-60000') matchesPrice = product.price >= 40000 && product.price <= 60000;
        else if (priceRange === '60000+') matchesPrice = product.price > 60000;

        return matchesSearch && matchesBrand && matchesPrice;
    });

    renderProducts(filtered);
}

// View Product Details
function viewProductDetails(productId) {
    const product = productsData.find(p => p.id === productId);
    if (!product) return;

    // Create detailed product view
    alert(`
${product.brand} ${product.model}

Processor: ${product.specs.processor}
RAM: ${product.specs.ram}
Storage: ${product.specs.storage}

Condition: ${product.condition}
Warranty: ${product.warranty}
Price: ₹${product.price.toLocaleString()}

Rating: ${product.rating}/5 (${product.reviews} reviews)

Click OK to add to cart or Cancel to continue shopping.
    `);
}

// Scroll to Products
function scrollToProducts() {
    const productsSection = document.getElementById('products');
    if (productsSection) {
        productsSection.scrollIntoView({ behavior: 'smooth' });
    }
}

// Cart Management
function addToCart(productId, productName, price) {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    
    const existingItem = cart.find(item => item.id === productId);
    if (existingItem) {
        existingItem.quantity++;
    } else {
        cart.push({
            id: productId,
            name: productName,
            price: price,
            quantity: 1
        });
    }

    localStorage.setItem('cart', JSON.stringify(cart));
    updateCartCount();
    
    // Show success message
    const message = document.createElement('div');
    message.className = 'success-message';
    message.textContent = '✓ Added to cart!';
    message.style.position = 'fixed';
    message.style.top = '80px';
    message.style.right = '20px';
    message.style.zIndex = '2000';
    message.style.animation = 'slideUp 0.3s ease';
    document.body.appendChild(message);
    
    setTimeout(() => message.remove(), 3000);
}

function updateCartCount() {
    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    const totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);
    if (cartCount) {
        cartCount.textContent = totalItems;
    }
}

function openCart() {
    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    const cartItems = document.getElementById('cartItems');
    
    if (!cartItems) return;

    if (cart.length === 0) {
        cartItems.innerHTML = '<div class="cart-empty">Your cart is empty</div>';
    } else {
        cartItems.innerHTML = cart.map(item => `
            <div class="cart-item">
                <div class="cart-item-image">💻</div>
                <div class="cart-item-details">
                    <div class="cart-item-title">${item.name}</div>
                    <div class="cart-item-spec">Qty: ${item.quantity}</div>
                </div>
                <div class="cart-item-price">₹${(item.price * item.quantity).toLocaleString()}</div>
                <button class="cart-item-remove" onclick="removeFromCart(${item.id})">
                    <i class="fas fa-trash"></i>
                </button>
            </div>
        `).join('');
    }

    // Update summary
    const subtotal = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
    document.getElementById('subtotal').textContent = '₹' + subtotal.toLocaleString();
    document.getElementById('total').textContent = '₹' + subtotal.toLocaleString();

    cartModal.classList.add('show');
}

function closeCart() {
    cartModal.classList.remove('show');
}

function removeFromCart(productId) {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    cart = cart.filter(item => item.id !== productId);
    localStorage.setItem('cart', JSON.stringify(cart));
    updateCartCount();
    openCart(); // Refresh cart display
}

function goToCheckout() {
    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    if (cart.length === 0) {
        alert('Your cart is empty!');
        return;
    }
    
    // Redirect to checkout page
    window.location.href = 'pages/checkout.html';
}

// Auth Modal Functions
function openAuthModal() {
    authModal.classList.add('show');
}

function closeAuthModal() {
    authModal.classList.remove('show');
    // Reset forms
    document.getElementById('customerLoginForm').reset();
    document.getElementById('customerRegisterForm').reset();
    document.getElementById('adminLoginForm').reset();
}

function switchAuthTab(tabName) {
    // Hide all tabs
    document.querySelectorAll('.auth-tab-content').forEach(tab => {
        tab.classList.remove('active');
    });
    document.querySelectorAll('.auth-tab-btn').forEach(btn => {
        btn.classList.remove('active');
    });

    // Show selected tab
    const tab = document.getElementById(tabName + 'Tab');
    if (tab) {
        tab.classList.add('active');
    }

    // Mark button as active
    const buttons = document.querySelectorAll('.auth-tab-btn');
    if (tabName === 'login') buttons[0].classList.add('active');
    else if (tabName === 'register') buttons[1].classList.add('active');
    else if (tabName === 'admin') buttons[2].classList.add('active');
}

// Auth Functions - Connected to Backend
async function handleCustomerLogin(event) {
    event.preventDefault();
    const email = document.getElementById('loginEmail').value;
    const password = document.getElementById('loginPassword').value;

    if (!email || !password) {
        alert('Please enter email and password');
        return;
    }

    try {
        const response = await fetch(`${API_URL}/customer/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password })
        });

        const data = await response.json();

        if (data.success) {
            localStorage.setItem('authToken', data.token);
            localStorage.setItem('user', JSON.stringify(data.customer));
            alert('✅ Login successful!');
            location.reload();
        } else {
            alert('❌ ' + data.message);
        }
    } catch (error) {
        alert('❌ Login failed: ' + error.message);
    }
}

async function handleCustomerRegister(event) {
    event.preventDefault();
    const name = document.getElementById('registerName').value;
    const email = document.getElementById('registerEmail').value;
    const password = document.getElementById('registerPassword').value;
    const phone = document.getElementById('registerPhone').value;

    if (!name || !email || !password || !phone) {
        alert('Please fill in all fields');
        return;
    }

    try {
        const response = await fetch(`${API_URL}/customer/register`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name, email, password, phone })
        });

        const data = await response.json();

        if (data.success) {
            localStorage.setItem('authToken', data.token);
            localStorage.setItem('user', JSON.stringify(data.customer));
            alert('✅ Registration successful!');
            location.reload();
        } else {
            alert('❌ ' + data.message);
        }
    } catch (error) {
        alert('❌ Registration failed: ' + error.message);
    }
}

async function handleAdminLogin(event) {
    event.preventDefault();
    const username = document.getElementById('adminUsername').value;
    const password = document.getElementById('adminPassword').value;

    if (!username || !password) {
        alert('Please enter username and password');
        return;
    }

    try {
        const response = await fetch(`${API_URL}/admin/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });

        const data = await response.json();

        if (data.success) {
            // Save token and admin info
            localStorage.setItem('adminToken', data.token);
            localStorage.setItem('admin', JSON.stringify(data.admin));
            // Mark admin session so admin.html can allow access
            sessionStorage.setItem('adminLoggedIn', 'true');
            sessionStorage.setItem('adminUsername', data.admin.username || username);
            alert('✅ Admin login successful! Redirecting to dashboard...');
            window.location.href = 'pages/admin.html';
        } else {
            alert('❌ ' + data.message);
        }
    } catch (error) {
        alert('❌ Admin login failed: ' + error.message);
    }
}

function handleOtpLogin(event) {
    event.preventDefault();
    alert('OTP login - SMS service integration needed');
}

function handleAdminOtpLogin(event) {
    event.preventDefault();
    alert('OTP login - SMS service integration needed');
}

function sendOtpCustomer() {
    const phone = document.getElementById('otpPhone').value;
    if (!phone) {
        alert('Please enter phone number');
        return;
    }
    alert('Demo: OTP will be sent to ' + phone);
    document.getElementById('otpCode').style.display = 'block';
    document.getElementById('verifyOtpBtn').style.display = 'block';
}

function sendOtpAdmin() {
    const username = document.getElementById('adminOtpUsername').value;
    const phone = document.getElementById('adminOtpPhone').value;
    if (!username || !phone) {
        alert('Please enter username and phone');
        return;
    }
    alert('Demo: OTP will be sent to ' + phone);
    document.getElementById('adminOtpCode').style.display = 'block';
    document.getElementById('verifyAdminOtpBtn').style.display = 'block';
}

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
