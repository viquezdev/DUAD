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


export async function getProductById(id) {
  const url = `http://localhost:5000/products/products/${id}`;

  const response = await axios.get(url);

  return response.data;
}

