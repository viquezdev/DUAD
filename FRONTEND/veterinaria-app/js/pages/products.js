import { getProducts } from "../api/productApi.js";
import { renderProducts,setupCardClicks } from "../ui/renderProducts.js";
import { setupNavbar, renderNavbar } from "../ui/navbar.js";
import { updateCartCount } from "../ui/navbar.js";

setupNavbar();
renderNavbar();
loadProducts();
updateCartCount();


async function loadProducts() {
  try {
    const products = await getProducts();

    renderProducts(products);
    setupCardClicks(products);
  } catch (error) {
    console.log(error);
  }
}
