import { removeFromCart} from "../services/cartService.js";
import { updateCartCount } from "./navbar.js";
import { getCart } from "../services/cartService.js";

export function renderCart(cart) {
  const container = document.querySelector("#cartContainer");

  if (cart.length === 0) {
    container.innerHTML = "<p>Carrito vacío</p>";
    document.querySelector("#total").textContent = "";
    return;
  }

  container.innerHTML = cart.map(item => `
    <div class="cart-item">
      <h3>${item.name}</h3>
      <p>Precio: ₡ ${item.price}</p>
      <p>Cantidad: ${item.quantity}</p>
      <button class="btn-remove" data-id="${item.id}">
        Eliminar
      </button>
    </div>
  `).join("");


  const total = cart.reduce((acc, item) => {
    return acc + item.price * item.quantity;
  }, 0);

  document.querySelector("#total").textContent = "Total: ₡ " + total;


  setupRemove();
}


export function setupRemove() {

  
  document.querySelectorAll(".btn-remove").forEach(btn => {
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