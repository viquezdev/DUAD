import { setupNavbar, renderNavbar } from "../ui/navbar.js";
import { getSession } from "../services/sessionService.js";
import { updateCartCount } from "../ui/navbar.js";
import {
  registerProduct,
  deleteProductById,
  getProductById,
} from "../api/productApi.js";
import { showProducts,showSales } from "../ui/renderAdmin.js";


const session = getSession();

if (!session || !session.user || !session.user.is_admin) {
  window.location.replace("index.html");
  throw new Error("Unauthorized");
}

setupNavbar();
renderNavbar();
showProducts();
showSales();

const form = document.querySelector(".addProductForm");
const message = document.querySelector(".error-message");
const errorMessage = document.querySelector("#adminError");

form.addEventListener("submit", async function (event) {
  event.preventDefault();
  errorMessage.textContent = "";
  const sku = document.querySelector("#sku").value.trim();
  const name = document.querySelector("#name").value.trim();
  const price = document.querySelector("#price").value;
  const description = document.querySelector("#description").value.trim();
  const quantity = document.querySelector("#quantity").value;

  try {
    await registerProduct(sku, name, price, description, quantity);

    await showProducts();

    this.reset();
    alert("Producto registrado exitosamente");
  } catch (error) {
    if (error.response) {
      errorMessage.textContent =
        error.response.data.error || "Error al registrar producto";
    } else {
      errorMessage.textContent = "Error al conectar con servidor";
    }
  }
});



const tableBody = document.querySelector("#productsTableBody");

tableBody.addEventListener("click", async function (event) {
  if (event.target.classList.contains("btn-delete")) {
    const productId = event.target.dataset.id;

    const confirmDelete = confirm("¿Seguro que deseas eliminar este producto?");

    if (!confirmDelete) return;

    try {
      await deleteProductById(productId);

      alert("Producto eliminado");

      await showProducts();
    } catch (error) {
      if (error.response) {
      errorMessage.textContent =
        error.response.data.error || "No fue posible eliminar el producto";
      } else {
        errorMessage.textContent = "No fue posible conectar con el servidor";
      }
      errorMessage.classList.add("show");
    }
  }

  if (event.target.classList.contains("btn")) {
    const productId = event.target.dataset.id;

    const confirmEdit = confirm("¿Seguro que deseas editar este producto?");

    if (!confirmEdit) return;

    window.location.href = `edit-product.html?id=${productId}`;
  }
});

