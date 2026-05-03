import { getCart, removeFromCart } from "../services/cartService.js";
import { renderCart } from "../ui/renderCart.js";
import { setupNavbar,renderNavbar } from "../ui/navbar.js";
import { updateCartCount } from "../ui/navbar.js";

setupNavbar();
renderNavbar();
loadCart();
updateCartCount();


function loadCart() {
  const cart = getCart();
  renderCart(cart);
}