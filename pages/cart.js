// Minimal placeholder to avoid 404. Implement cart functions here if needed.
console.log('cart.js loaded');

function getCart() {
    try {
        const cart = localStorage.getItem('cart');
        return cart ? JSON.parse(cart) : [];
    } catch (e) {
        return [];
    }
}

function saveCart(cart) {
    try {
        localStorage.setItem('cart', JSON.stringify(cart || []));
    } catch (e) {}
}
