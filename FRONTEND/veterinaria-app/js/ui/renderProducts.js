export function renderProducts(products) {
  const container = document.querySelector("#productsContainer");

  container.innerHTML = products
    .map(
      (product) => `
    <div class="product-card">
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
