export async function getProducts() {
  try {
    const url = "http://localhost:5000/products/products";

    const response = await axios.get(url);
    console.log(response.data);
    return response.data;
  } catch (error) {
    console.log(error);
    throw error;
  }
}


export async function getCartById(id) {
  const url = `http://localhost:5000/shopping_carts/shopping_carts/${id}`;

  const response = await axios.get(url);

  return response.data;
}

export async function addProductToCart(cartId,productId,quantity) {
  try {
    const url = `http://localhost:5000/shopping_carts/shopping_carts/${cartId}/products`;

    const cartData = {
      productId: productId,
      quantity: quantity,
    };

    const response = await axios.post(url, cartData);

    const data = response.data;
    saveSession(data);
    alert("Login exitoso");
    window.location.href = "index.html";
    console.log(data);

  } catch (error) {
    console.log(error);

    if (error.response) {
      message.textContent = error.response.data.message;
    } else {
      message.textContent = "Error al conectar con el servidor";
    }
  }
}