import { getProducts } from "../api/productApi.js";
import { getSales } from "../api/salesApi.js";

export async function showProducts() {
  
  try {
    const products = await getProducts();

    const tableBody = document.querySelector("#productsTableBody");

    tableBody.innerHTML = products
      .map(
        (product) => `

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

      `,
      )
      .join("");
  } catch (error) {
    if (error.response) {
      errorMessage.textContent =
        error.response.data.error || "No fue posible cargar los productos";
    } else {
      errorMessage.textContent = "No fue posible conectar con el servidor";
    }
    errorMessage.classList.add("show");
  }
}


export async function showSales() {
  const errorMessage = document.querySelector("#adminError");
  try {
    const sales = await getSales();
    const tableBody = document.querySelector("#salesTableBody");

    tableBody.innerHTML = sales
      .map(
        (sale) => `

        <tr>

          <td>${sale.invoice_number}</td>

          <td>${sale.created_at}</td>

          <td> ${sale.username} </td>

          <td>${sale.payment_method}</td>

          <td>${sale.payment_status}</td>

          <td>${sale.total_amount}</td>
        </tr>

      `,
      )
      .join("");
  } catch (error) {
    if (error.response) {
      errorMessage.textContent =
        error.response.data.error || "No fue posible cargar las ventas";
    } else {
      errorMessage.textContent = "No fue posible conectar con el servidor";
    }
    errorMessage.classList.add("show");
  }
}
