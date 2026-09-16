import axios from 'axios';

const API_URL = `${import.meta.env.VITE_API_URL}/shopping_carts/shopping_carts`;

export const getCartService = async (userId, token) => {
  try {
    const response = await axios.get(`${API_URL}/${userId}`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    return response.data;
  } catch (error) {
    if (error.response?.status === 404) {
      return null;
    }

    throw error;
  }
};

export const addToCartService = async (
  cart_id,
  product_id,
  quantity,
  token
) => {
  try {
    const response = await axios.post(
      `${API_URL}/${cart_id}/products`,
      { product_id, quantity },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    return response.data;
  } catch (error) {
    console.error('Error al agregar producto al carrito:', error);
    throw error;
  }
};

export const removeFromCartService = async (cartId, productId, token) => {
  try {
    await axios.delete(`${API_URL}/${cartId}/products/${productId}`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
  } catch (error) {
    console.error('Error al eliminar producto del carrito:', error);
    throw error;
  }
};

export const updateCartItemService = async (
  cartId,
  productId,
  quantity,
  token
) => {
  try {
    const response = await axios.patch(
      `${API_URL}/${cartId}/products/${productId}`,
      { quantity },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    return response.data;
  } catch (error) {
    console.error('Error al actualizar producto en el carrito:', error);
    throw error;
  }
};

export const createCartService = async (user_id, status, token) => {
  try {
    const response = await axios.post(
      API_URL,
      { user_id, status },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    return response.data;
  } catch (error) {
    console.error('Error al crear el carrito:', error);
    throw error;
  }
};

export const deleteCartService = async (cartId, token) => {
  try {
    await axios.delete(`${API_URL}/${cartId}`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
  } catch (error) {
    console.error('Error al eliminar el carrito:', error);
    throw error;
  }
};

export const getCartItemsService = async (cartId, token) => {
  try {
    const response = await axios.get(`${API_URL}/${cartId}/products`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    return response.data;
  } catch (error) {
    console.error('Error al obtener los productos del carrito:', error);
    throw error;
  }
};
