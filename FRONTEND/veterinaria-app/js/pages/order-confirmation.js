import { setupNavbar, renderNavbar } from "../ui/navbar.js";
import { updateCartCount } from "../ui/navbar.js";
import { getSession } from "../services/sessionService.js";

const session = getSession();

if (!session || !session.user || !session.user.is_admin) {
  window.location.replace("index.html");
  throw new Error("Unauthorized");
}

setupNavbar();
renderNavbar();

renderSummary()

function renderSummary() {
  const orderData =JSON.parse(localStorage.getItem("lastOrder"));

  if (!orderData) {
  window.location.href = "products.html";
  }

  const summaryContainer =document.querySelector("#summaryContainer");

  const subtotalElement =document.querySelector("#subtotal");

  const totalElement =document.querySelector("#checkoutTotal");

  const formatter =
  new Intl.NumberFormat("es-CR", {
    style: "currency",
    currency: "CRC",
  });

  summaryContainer.innerHTML =
  orderData.products
    .map(
      (product) => `
      <div class="summary-product">
        <div>
          <h3>${product.name}</h3>

          <p>
            Cantidad:
            ${product.quantity}
          </p>
        </div>

        <p>
          ${formatter.format(
            product.price * product.quantity
          )}
        </p>
      </div>
    `,
    )
    .join("");

  subtotalElement.textContent =formatter.format(orderData.total);

  totalElement.textContent =formatter.format(orderData.total);

 
}


document.querySelector("#btn-products").addEventListener("click", () => {
    window.location.href = "products.html";
  });

document.querySelector(".btn-index").addEventListener("click", () => {
    window.location.href = "index.html";
  });