import { renderNavbar, setupNavbar } from "../ui/navbar.js";

setupNavbar();
renderNavbar();

const btnProducts = document.querySelector("#btn-products");
btnProducts.addEventListener("click", () => {
  window.location.href = "products.html";
});
