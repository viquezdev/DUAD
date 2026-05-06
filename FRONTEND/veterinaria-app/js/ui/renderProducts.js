import { addToCart } from "../services/cartService.js";
import { getSession } from "../services/sessionService.js";
import { updateCartCount } from "./navbar.js";


export function renderProducts(products) {
  const container = document.querySelector("#productsContainer");

  container.innerHTML = products
    .map(
      (product) => `
    <div class="product-card" data-id="${product.id}">
      <h2>${product.name}</h2>

      <p>${product.description}</p>

      <p class="price">
        ₡ ${Number(product.price).toFixed(2)}
      </p>

      <p>Stock: ${product.quantity}</p>

      <button class="btn">
        Agregar al carrito
      </button>
    </div>
  `,
    )
    .join("");
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
      <p>Stock: ${product.quantity}</p>
      <button class="btn">Agregar al carrito</button>
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