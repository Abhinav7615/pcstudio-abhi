// Auth shim for scripts under js/
console.log('js/auth.js loaded');

function setToken(token) {
    try { localStorage.setItem('adminToken', token); } catch (e) {}
}

function getToken() {
    try { return localStorage.getItem('adminToken'); } catch (e) { return null; }
}

function clearToken() {
    try { localStorage.removeItem('adminToken'); sessionStorage.removeItem('adminLoggedIn'); } catch (e) {}
}

function isAdminLoggedIn() {
    try { return sessionStorage.getItem('adminLoggedIn') === 'true' && !!getToken(); } catch (e) { return false; }
}

function requireAdminLogin() {
    if (!isAdminLoggedIn()) {
        window.location.href = '/pages/admin-login.html';
    }
}

function getAuthHeaders() {
    const token = getToken();
    const headers = { 'Content-Type': 'application/json' };
    if (token) headers['Authorization'] = `Bearer ${token}`;
    return headers;
}

async function apiFetch(path, options = {}) {
    const API_URL = (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1')
        ? 'http://127.0.0.1:5000/api' : 'https://pcstudio-abhi-1.onrender.com/api';
    const url = path.startsWith('http') ? path : `${API_URL}${path}`;
    options.headers = Object.assign({}, getAuthHeaders(), options.headers || {});
    try {
        const res = await fetch(url, options);
        if (res.status === 401) {
            clearToken();
            window.location.href = '/pages/admin-login.html';
            return null;
        }
        return res;
    } catch (e) {
        throw e;
    }
}
