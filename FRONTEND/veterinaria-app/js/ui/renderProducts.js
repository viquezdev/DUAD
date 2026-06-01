import { addToCart } from "../services/cartService.js";
import { getSession } from "../services/sessionService.js";
import { updateCartCount } from "./navbar.js";


export function renderProducts(products) {
  const container = document.querySelector("#productsContainer");

  const formatter = new Intl.NumberFormat("es-CR", {
    style: "currency",
    currency: "CRC",
  });

  if(products){
    container.classList.add("products-grid");
    container.innerHTML = products
    .map(
      (product) => `
    <div class="product-card" data-id="${product.id}">
      <h2>${product.name}</h2>

      <p>${product.description}</p>

      <p class="price">
        ${formatter.format(Number(product.price))}
      </p>

      <p class="${
        product.quantity === 0 ? "out-stock" : "in-stock"
      }">
        ${
          product.quantity === 0
            ? "Agotado"
            : `Stock: ${product.quantity}`
        }
      </p>

      <button 
        class="btn"
        ${product.quantity === 0 ? "disabled" : ""}
      >
        ${
          product.quantity === 0
            ? "Sin stock"
            : "Agregar al carrito"
        }
      </button>
    </div>
  `,
    )
    .join("");
  }
  else{
    container.classList.remove("products-grid");
    container.innerHTML = `
      <div class="empty-container">
      <div class="empty-catalog">
        <img src="assets/icons/stock-out.svg" class="empty-catalog-img"/>
        <h2>El catálogo está vacío</h2>
        <p>No existen productos disponibles.</p>
        <a href="index.html" class="btn-products">Ir a inicio</a>
      </div></div>
    `;
  }
  
}


export function setupCardClicks(products) {
  const container = document.querySelector("#productsContainer");
  const session=getSession();

  if (!container) return;

  container.addEventListener("click", (e) => {

  
    if (e.target.classList.contains("btn")) {

      if(session){

      e.stopPropagation();

      const card = e.target.closest(".product-card");
      const id = card.dataset.id;

      const product = products.find(p => p.id == id);

      addToCart(product);
      updateCartCount();
      alert("Producto agregado al carrito");
      }
      else{
        alert("Debes iniciar sesion para poder agregar productos al carrito");
      }
    }


    else {
      const card = e.target.closest(".product-card");

      if (!card) return;

      const id = card.dataset.id;

      window.location.href = `product.html?id=${id}`;
    }

  });
}

export function renderProduct(product) {
  const container = document.querySelector("#productDetail");

  container.innerHTML = `
    <div class="product-card">
      <h1>${product.name}</h1>
      <p>${product.description}</p>
      <p class="price">₡ ${Number(product.price).toFixed(2)}</p>
      <p class="${
        product.quantity === 0 ? "out-stock" : "in-stock"
      }">
        ${
          product.quantity === 0
            ? "Agotado"
            : `Stock: ${product.quantity}`
        }
      </p>

      <button 
        class="btn"
        ${product.quantity === 0 ? "disabled" : ""}
      >
        ${
          product.quantity === 0
            ? "Sin stock"
            : "Agregar al carrito"
        }
      </button>
      <a href="products.html">Regresar al catálogo de productos</a>
    </div>
  `;
}


export function setupProductClick(product) {
  const container = document.querySelector("#productDetail");
  const session=getSession();

  if (!container) return;

  container.addEventListener("click", (e) => {

  
    if (e.target.classList.contains("btn")) {

      if(session){
      addToCart(product);
      updateCartCount();
      alert("Producto agregado al carrito");
      }
      else{
        alert("Debes iniciar sesion para poder agregar productos al carrito");
      }
    }



  });
}