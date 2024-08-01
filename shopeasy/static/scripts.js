function addToCart(productId) {
    fetch('/api/cart', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ product_id: productId }),
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        updateCartCount(data.cart_count);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function removeFromCart(productId) {
    fetch('/api/cart/remove', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ product_id: productId }),
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        updateCartCount(data.cart_count);
        location.reload();
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function updateCartCount(count) {
    const cartCountElement = document.getElementById('cart-count');
    if (cartCountElement) {
        cartCountElement.textContent = count;
    }
}
