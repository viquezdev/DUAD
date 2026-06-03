import { getCart, removeFromCart } from "../services/cartService.js";
import { renderCart } from "../ui/renderCart.js";
import { setupNavbar,renderNavbar } from "../ui/navbar.js";
import { updateCartCount } from "../ui/navbar.js";

setupNavbar();
renderNavbar();
loadCart();
updateCartCount();


function loadCart() {
  const errorMessage = document.querySelector("#errorMessage");
  try {
    const cart = getCart();
    renderCart(cart);
  } catch (error) {
    if (error.response) {
      errorMessage.textContent = error.response.data.error || "No se pudo cargar el carrito";
    } else {
      errorMessage.textContent = "No fue posible conectar con el servidor";
    }
  }
  
}

const btnCheckout = document.querySelector(".btn-checkout");
btnCheckout.addEventListener("click", () => {
  window.location.href = "checkout.html";
});