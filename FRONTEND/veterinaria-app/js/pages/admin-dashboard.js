import { setupNavbar, renderNavbar } from "../ui/navbar.js";
import { getSession } from "../services/sessionService.js";
import { updateCartCount } from "../ui/navbar.js";
import { registerProduct,getProducts,deleteProductById } from "../api/productApi.js";

setupNavbar();
renderNavbar();
showProducts();

const form = document.querySelector(".addProductForm");
const message = document.querySelector(".error-message");

form.addEventListener("submit", async function (event) {
  event.preventDefault();

  const sku = document.querySelector("#sku").value.trim();
  const name = document.querySelector("#name").value.trim();
  const price = document.querySelector("#price").value;
  const description = document.querySelector("#description").value.trim();
  const quantity = document.querySelector("#quantity").value;

  message.textContent = "";

  try {
    await registerProduct(
      sku,
      name,
      price,
      description,
      quantity
    );

    await showProducts();

    this.reset();
    alert("Producto registrado exitosamente");

  } catch (error) {

    if (error.response) {

      message.textContent =
        error.response.data.error ||
        "Error al registrar producto";

    } else {

      message.textContent =
        "Error al conectar con servidor";
    }
  }
});




async function showProducts() {

  try {

    const products = await getProducts();

    const tableBody = document.querySelector("#productsTableBody");

    tableBody.innerHTML = products
      .map((product) => `

        <tr>

          <td>${product.id}</td>

          <td>${product.name}</td>

          <td>
            ₡ ${Number(product.price).toFixed(2)}
          </td>

          <td>${product.quantity}</td>

          <td>

            <button
              class="btn"
              data-id="${product.id}"
            >
              Editar
            </button>

            <button
              class="btn-delete"
              data-id="${product.id}"
            >
              Eliminar
            </button>

          </td>

        </tr>

      `)
      .join("");

  } catch (error) {

    console.log(error);
  }
}


const tableBody = document.querySelector("#productsTableBody");

tableBody.addEventListener("click", async function (event) {

  if (event.target.classList.contains("btn-delete")) {

    const productId = event.target.dataset.id;

    const confirmDelete = confirm("¿Seguro que deseas eliminar este producto?");

    if (!confirmDelete) return;

    try {

      await deleteProductById(productId);

      alert("Producto eliminado");

      showProducts();

    }
    catch (error) {

      console.log(error);

      alert("Error eliminando producto");
    }
  }


  if (event.target.classList.contains("btn")) {

    const productId = event.target.dataset.id;

    console.log("Editar producto:", productId);

  }

});

