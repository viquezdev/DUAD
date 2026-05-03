export function getCart() {
  return JSON.parse(localStorage.getItem("cart")) || [];
}

export function saveCart(cart) {
  localStorage.setItem("cart", JSON.stringify(cart));
}

export function addToCart(product) {
  const cart = getCart();

  const existing = cart.find(item => item.id === product.id);

  if (existing) {
    existing.quantity += 1;
  } else {
    cart.push({
      id: product.id,
      name: product.name,
      price: Number(product.price),
      quantity: 1
    });
  }

  saveCart(cart);
}


export function removeFromCart(id) {
  const cart = getCart().filter(item => item.id != id);
  saveCart(cart);
}



export function getCartCount() {
  const cart = getCart();

  return cart.reduce((acc, item) => {
    return acc + item.quantity;
  }, 0);
}