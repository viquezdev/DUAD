import { getSession } from "../services/sessionService.js";




export async function getProducts() {
  const response = await axios.get(
    "http://localhost:5000/products/products"
  );
  return response.data;
}

export async function getProductById(id) {
  const response = await axios.get(
  `http://localhost:5000/products/products/${id}`
  );
  return response.data;
}

export async function registerProduct(sku, name, price, description, quantity) {
  const session = getSession();
  if (!session) {
    throw new Error("No existe una sesión activa");
  }
  const token = session.access_token;
  const url = "http://localhost:5000/products/products";

  const productData = {
    sku: sku,
    name: name,
    price: price,
    description: description,
    quantity: quantity,
  };

  const response = await axios.post(url, productData, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

    return response.data;
  
}

export async function deleteProductById(id) {
  const session = getSession();  
  if (!session) {
      throw new Error("No existe una sesión activa");
    }
    const token = session.access_token;
    const url = `http://localhost:5000/products/products/${id}`;
    const response = await axios.delete(url, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    return response.data;
}

export async function updateProduct(id,sku,name,price,description,quantity,) {
    const session = getSession();
    if (!session) {
      throw new Error("No existe una sesión activa");
    }
    const token = session.access_token;

    const url = `http://localhost:5000/products/products/${id}`;

    const productData = {
      sku: sku,
      name: name,
      price: price,
      description: description,
      quantity: quantity,
    };

    const response = await axios.put(url, productData, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    return response.data;
}
