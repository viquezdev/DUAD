import { getProductById } from "../api/productApi.js";
import { setupNavbar, renderNavbar } from "../ui/navbar.js";
import { updateProduct } from "../api/productApi.js";
import { getSession } from "../services/sessionService.js";

setupNavbar();
renderNavbar();

const session = getSession();
console.log(session);
if (!session || !session.user || !session.user.is_admin) {
  window.location.replace("index.html");
  throw new Error("Unauthorized");
}

const form = document.querySelector(".addProductForm");
const message = document.querySelector(".error-message");

const skuEdit = document.querySelector("#skuEdit");

const nameEdit = document.querySelector("#nameEdit");

const priceEdit = document.querySelector("#priceEdit");

const descriptionEdit = document.querySelector("#descriptionEdit");

const quantityEdit = document.querySelector("#quantityEdit");

const params = new URLSearchParams(window.location.search);



async function loadProduct() {

  try {

    

    const productId = params.get("id");

    const product = await getProductById(productId);

    skuEdit.value = product.sku;

    nameEdit.value = product.name;

    priceEdit.value = product.price;

    descriptionEdit.value = product.description;

    quantityEdit.value = product.quantity;

  } catch (error) {

    console.log(error);

    alert("Error cargando producto");
  }
}

loadProduct();


form.addEventListener("submit",async function (event) {

    event.preventDefault();

    const productId = params.get("id");

    const sku = document.querySelector("#skuEdit").value;

    const name = document.querySelector("#nameEdit").value;

    const price = document.querySelector("#priceEdit").value;

    const description = document.querySelector("#descriptionEdit").value;

    const quantity = document.querySelector("#quantityEdit").value;

    try {
      console.log(productId);
      await updateProduct(
        productId,
        sku,
        name,
        price,
        description,
        quantity
      );

      alert("Producto actualizado");

      window.location.href =
        "admin-dashboard.html";

    } catch (error) {

      console.log(error);

      alert("Error actualizando producto");
    }
  }
);