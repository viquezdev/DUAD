export async function createCart(cartData) {
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


