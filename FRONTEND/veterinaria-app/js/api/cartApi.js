

import { getSession } from "../services/sessionService.js";

const session = getSession();

export async function createCart(cartData) {

    if (!session) {
      throw new Error("No existe una sesión activa");
    }
    const token = session.access_token;

    const url =
      "http://localhost:5000/checkout/checkout";

    const response = await axios.post(
      url,
      cartData,
      {
        headers: {
          Authorization: `Bearer ${token}`
        }
      }
    );

    return response.data;

}