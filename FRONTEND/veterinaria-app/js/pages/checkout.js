import { setupNavbar,renderNavbar } from "../ui/navbar.js";
import { getCart } from "../services/cartService.js";

setupNavbar();
renderNavbar();


loadCheckout();

function loadCheckout() {

  const cart = getCart();

  renderSummary(cart);
}

function renderSummary(cart) {

  const container = document.querySelector("#summaryContainer");

  container.innerHTML = cart.map(item => `
  
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

  `).join("");

  const subtotal = cart.reduce((acc, item) => {
    return acc + item.price * item.quantity;
  }, 0);

  document.querySelector("#subtotal").textContent =
    "₡" + subtotal.toFixed(2);

  document.querySelector("#checkoutTotal").textContent =
    "₡" + subtotal.toFixed(2);
}