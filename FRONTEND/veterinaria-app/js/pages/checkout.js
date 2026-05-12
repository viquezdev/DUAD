import { setupNavbar, renderNavbar } from "../ui/navbar.js";
import { getCart } from "../services/cartService.js";
import { updateCartCount } from "../ui/navbar.js";

import { createCart } from "../api/cartApi.js";

setupNavbar();
renderNavbar();
updateCartCount();

loadCheckout();

function loadCheckout() {
  const cart = getCart();

  renderSummary(cart);
}

function renderSummary(cart) {
  const container = document.querySelector("#summaryContainer");

  container.innerHTML = cart
    .map(
      (item) => `
  
    <div class="summary-item">

      <div class="itemCart">

        <p>${item.name}</p>

        <small>
          ${item.quantity} x ₡${item.price}
        </small>

      </div>
    <div>
      <strong>
        ₡${(item.price * item.quantity).toFixed(2)}
      </strong>
  </div>
    </div>

  `,
    )
    .join("");

  const subtotal = cart.reduce((acc, item) => {
    return acc + item.price * item.quantity;
  }, 0);

  document.querySelector("#subtotal").textContent = "₡" + subtotal.toFixed(2);

  document.querySelector("#checkoutTotal").textContent =
    "₡" + subtotal.toFixed(2);
}

const confirmBtn = document.querySelector("#btnConfirm");

confirmBtn.addEventListener("click", confirmCheckout);

async function confirmCheckout() {
  try {
    const cart = getCart();

    if (cart.length === 0) {
      alert("El carrito está vacío");
      return;
    }

    const address = document.querySelector("#address").value;

    const paymentMethod = document.querySelector("#paymentMethod").value;

    if (!address || !paymentMethod) {
      alert("Completa todos los campos");
      return;
    }

    const total = cart.reduce((acc, item) => {
      return acc + item.price * item.quantity;
    }, 0);

    const products = cart.map((item) => ({
      id: item.id,
      quantity: item.quantity,
    }));

    const checkoutData = {
      billing_address: address,

      payment_method: paymentMethod,

      total_amount: total,

      products: products,
    };

    createCart(checkoutData);
  } catch (error) {
    console.log(error);

    alert("Error al procesar compra");
  }
}
