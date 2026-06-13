import { getProducts } from "../api/productApi.js";
import { renderProducts,setupCardClicks } from "../ui/renderProducts.js";
import { setupNavbar, renderNavbar } from "../ui/navbar.js";
import { updateCartCount } from "../ui/navbar.js";

setupNavbar();
renderNavbar();
loadProducts();
updateCartCount();

const errorMessage = document.querySelector("#productsError");

async function loadProducts() {
  try {
    const products = await getProducts();

    renderProducts(products);
   
    setupCardClicks(products);
  } catch (error) {
    if (error.response) {
      errorMessage.textContent = error.response.data.error || "No fue posible cargar los productos";
    } else {
      errorMessage.textContent = "No fue posible conectar con el servidor";

    }
     errorMessage.classList.add("show");
  }
}
