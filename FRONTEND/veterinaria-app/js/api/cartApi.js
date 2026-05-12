

import { getSession } from "../services/sessionService.js";



export async function createCart(cartData) {

  try {

    const session = getSession();

    const token = session.access_token;

    const url =
      "http://localhost:5000/shopping_carts/shopping_carts";

    const response = await axios.post(
      url,
      cartData,
      {
        headers: {
          Authorization: `Bearer ${token}`
        }
      }
    );

    const data = response.data;

    console.log(data);

    return data;

  } catch (error) {

    console.log(error);

    throw error;
  }
}