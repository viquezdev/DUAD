import { getSession } from "../services/sessionService.js";



export async function getSales() {
  const session = getSession();
  if (!session) {
    throw new Error("No existe una sesión activa");
  }
  const token = session.access_token;
  const response = await axios.get(
    "http://localhost:5000/invoices/invoices",
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );

  return response.data;
}