import { getProductById } from "../api/productApi.js";
import { renderProduct } from "../ui/renderProducts.js";
import { setupNavbar,renderNavbar } from "../ui/navbar.js";
import { updateCartCount } from "../ui/navbar.js";

setupNavbar();
renderNavbar();
loadProduct();
updateCartCount();

async function loadProduct() {
  const params = new URLSearchParams(window.location.search);
  const id = params.get("id");

  const product = await getProductById(id);

  renderProduct(product);
}