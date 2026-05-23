
import { getSession } from "../services/sessionService.js";

const session=getSession();
const token=session.access_token;

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
  try {
    const url = `http://localhost:5000/products/products/${id}`;
    const response = await axios.get(url);
    return response.data;
  } catch (error) {
    console.log(error);
    throw error;
  }
  
}


export async function registerProduct(sku, name, price,description,quantity) {
  try {

    const url = "http://localhost:5000/products/products";

    const productData = {
      sku: sku,
      name: name,
      price: price,
      description:description,
      quantity:quantity
    };

    const response = await axios.post(
        url, 
        productData,
        {
        headers: {
          Authorization: `Bearer ${token}`
        }
      }
    );

    return response.data;

   } catch (error) {

    console.log(error);

    throw error;
  }
}


export async function deleteProductById(id) {
  try {
    const url = `http://localhost:5000/products/products/${id}`;
    const response = await axios.delete(
      url,
      {
        headers: {
          Authorization: `Bearer ${token}`
        }
      }
    );
    return response.data;
  } catch (error) {
    console.log(error);
    throw error;
  }
  
}
