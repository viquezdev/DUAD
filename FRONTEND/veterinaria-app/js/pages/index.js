import { renderNavbar, setupNavbar } from "../ui/navbar.js";
import { updateCartCount } from "../ui/navbar.js";


setupNavbar();
renderNavbar();
updateCartCount();

const btnProducts = document.querySelector("#btn-products");
btnProducts.addEventListener("click", () => {
  window.location.href = "products.html";
});
