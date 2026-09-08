import axios from 'axios';

const API_URL = `${import.meta.env.VITE_API_URL}/products/products`;

export const getProducts = async () => {
  const response = await axios.get(API_URL);
  return response.data;
};

export const createProductService = async (product, token) => {
  try {
    const response = await axios.post(API_URL, product, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    return response.data;
  } catch (error) {
    console.error('Error al crear producto:', error);
    throw error;
  }
};

export const updateProductService = async (id, product, token) => {
  try {
    const response = await axios.put(`${API_URL}/${id}`, product, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    return response.data;
  } catch (error) {
    console.error('Error al actualizar el producto:', error);
    throw error;
  }
};

export const deleteProductService = async (id, token) => {
  try {
    await axios.delete(`${API_URL}/${id}`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
  } catch (error) {
    console.error('Error al eliminar el producto:', error);
    throw error;
  }
};
