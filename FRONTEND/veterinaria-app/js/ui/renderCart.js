import { removeFromCart } from "../services/cartService.js";
import { updateCartCount } from "./navbar.js";
import { getCart } from "../services/cartService.js";

export function renderCart(cart) {
  const container = document.querySelector("#cartContainer");
  const checkoutContainer = document.querySelector(".totalContainer");
  if (cart.length === 0) {
    checkoutContainer.classList.add("hidden");
    container.innerHTML = `
      <div class="empty-cart">
        <img src="assets/icons/carrito.png" class="empty-cart-img"/>
        <h2>Tu carrito está vacío</h2>
        <p>Agrega productos desde el catálogo.</p>
        <a href="products.html" class="btn-products">Ver productos</a>
      </div>
    `;

    document.querySelector("#total").textContent = "";
    return;
  }
  checkoutContainer.classList.remove("hidden");
  container.innerHTML = cart
    .map(
      (item) => `
    
    <div class="cart-item">
      <h3>${item.name}</h3>
      <p>Precio: ₡ ${item.price}</p>
      <p>Cantidad: ${item.quantity}</p>
      <button class="btn-remove" data-id="${item.id}">
        Eliminar
      </button>
    </div>
  `,
    )
    .join("");

  const total = cart.reduce((acc, item) => {
    return acc + item.price * item.quantity;
  }, 0);

  document.querySelector("#total").textContent = "Total: ₡ " +Number(total.toFixed(2)) ;

  setupRemove();
}

export function setupRemove() {
  document.querySelectorAll(".btn-remove").forEach((btn) => {
    btn.addEventListener("click", () => {
      const id = btn.dataset.id;
      removeFromCart(id);
      updateCartCount();
      loadCart();
    });
  });
}

function loadCart() {
  const cart = getCart();
  renderCart(cart);
}
