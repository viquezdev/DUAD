import axios from 'axios';

const API_URL = `${import.meta.env.VITE_API_URL}/invoices/invoices`;

export const createInvoiceService = async (invoiceData, token) => {
  try {
    const response = await axios.post(API_URL, invoiceData, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    return response.data;
  } catch (error) {
    console.error('Error al crear la factura:', error);
    throw error;
  }
};
