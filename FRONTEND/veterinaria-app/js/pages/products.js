import { getProducts } from "../api/productApi.js";
import { renderProducts } from "../ui/renderProducts.js";
import { setupNavbar, renderNavbar } from "../ui/navbar.js";

setupNavbar();
renderNavbar();
loadProducts();

async function loadProducts() {
  try {
    const products = await getProducts();

    renderProducts(products);
  } catch (error) {
    console.log(error);
  }
}
