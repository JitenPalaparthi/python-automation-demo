from __future__ import annotations

import os

from flask import Flask, jsonify, render_template_string, request

app = Flask(__name__)

PRODUCTS = [
    {"id": 1, "name": "Laptop Bag", "price": 2499},
    {"id": 2, "name": "Wireless Mouse", "price": 1299},
    {"id": 3, "name": "Mechanical Keyboard", "price": 4999},
     {"id": 5, "name": "hdd", "price": 1255},
]

HTML = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Playwright Python Demo Shop</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 2rem; background: #f7f7fb; }
    .grid { display: grid; grid-template-columns: repeat(3, minmax(220px, 1fr)); gap: 1rem; }
    .card { background: white; padding: 1rem; border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,.08); }
    button { cursor: pointer; padding: .6rem .9rem; border: none;
             border-radius: 8px; background: #111827; color: white; }
    input { padding: .5rem; width: 280px; margin-right: .5rem; }
    .ok { color: #047857; }
    .err { color: #b91c1c; }
    header, section { margin-bottom: 2rem; }
  </style>
</head>
<body>
  <header>
    <h1>Demo Shop</h1>
    <p>Deterministic UI for Playwright Python automation training.</p>
  </header>

  <section aria-label="login-section">
    <h2>Login</h2>
    <label for="username">Username</label>
    <input id="username" name="username" value="student">
    <label for="password">Password</label>
    <input id="password" name="password" type="password" value="playwright123">
    <button id="login-btn">Login</button>
    <p id="login-message" role="status"></p>
  </section>

  <section aria-label="catalog-section">
    <h2>Catalog</h2>
    <div class="grid" id="product-list"></div>
  </section>

  <section aria-label="cart-section">
    <h2>Cart</h2>
    <p id="cart-count">Cart Items: 0</p>
    <button id="checkout-btn">Checkout</button>
    <p id="checkout-message" role="alert"></p>
  </section>

<script>
  const state = { cart: 0, loggedIn: false };

  async function loadProducts() {
    const response = await fetch('/api/products');
    const products = await response.json();
    const container = document.getElementById('product-list');
    container.innerHTML = '';
    products.forEach((product) => {
      const card = document.createElement('div');
      card.className = 'card';
      card.innerHTML = `
        <h3>${product.name}</h3>
        <p>₹${product.price}</p>
        <button data-testid="add-to-cart-${product.id}">Add to cart</button>
      `;
      card.querySelector('button').addEventListener('click', () => {
        state.cart += 1;
        document.getElementById('cart-count').textContent = `Cart Items: ${state.cart}`;
      });
      container.appendChild(card);
    });
  }

  document.getElementById('login-btn').addEventListener('click', async () => {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const response = await fetch('/api/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password })
    });
    const result = await response.json();
    const msg = document.getElementById('login-message');
    state.loggedIn = response.ok;
    msg.textContent = result.message;
    msg.className = response.ok ? 'ok' : 'err';
  });

  document.getElementById('checkout-btn').addEventListener('click', async () => {
    const response = await fetch('/api/checkout', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ cart_items: state.cart, logged_in: state.loggedIn })
    });
    const result = await response.json();
    document.getElementById('checkout-message').textContent = result.message;
  });

  loadProducts();
</script>
</body>
</html>
"""


@app.get("/")
def home() -> str:
    return render_template_string(HTML)


@app.get("/health")
def health() -> tuple[dict[str, str], int]:
    return {"status": "ok"}, 200


@app.get("/api/products")
def get_products() -> tuple:
    return jsonify(PRODUCTS), 200


@app.post("/api/login")
def login() -> tuple:
    payload = request.get_json(silent=True) or {}
    username = payload.get("username", "")
    password = payload.get("password", "")

    if username == "student" and password == "playwright123":
        return jsonify({"message": "Login successful"}), 200

    return jsonify({"message": "Invalid credentials"}), 401


@app.post("/api/checkout")
def checkout() -> tuple:
    payload = request.get_json(silent=True) or {}
    cart_items = int(payload.get("cart_items", 0))
    logged_in = bool(payload.get("logged_in", False))

    if not logged_in:
        return jsonify({"message": "Please login before checkout"}), 401

    if cart_items <= 0:
        return jsonify({"message": "Your cart is empty"}), 400

    return jsonify({"message": f"Order confirmed for {cart_items} item(s)"}), 200


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    app.run(host="0.0.0.0", port=port, debug=False)
