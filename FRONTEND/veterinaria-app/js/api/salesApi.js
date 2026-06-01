
import { getSession } from "../services/sessionService.js";

const session=getSession();
const token=session.access_token;

export async function getSales() {
  try {
    const url = "http://localhost:5000/invoices/invoices";

    const response = await axios.get(
      url,
      {
        headers: {
          Authorization: `Bearer ${token}`
        }
      }
    );
    console.log(response.data);
    return response.data;
  } catch (error) {
    console.log(error);
    throw error;
  }
}


