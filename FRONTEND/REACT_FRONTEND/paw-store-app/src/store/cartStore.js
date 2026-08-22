import { create } from 'zustand';

import {
  getCartService,
  addToCartService,
  removeFromCartService,
  updateCartItemService,
  createCartService,
  getCartItemsService,
  deleteCartService,
} from '../services/cartService';

import { useAuthStore } from './authStore';

export const useCartStore = create((set) => ({
  cart: null,
  cartItems: [],
  loading: false,
  error: null,

  loadCart: async (userId) => {
    set({
      loading: true,
      error: null,
    });

    try {
      const token = useAuthStore.getState().accessToken;

      const cart = await getCartService(userId, token);

      if (!cart) {
        set({
          cart: null,
          cartItems: [],
          loading: false,
        });

        return;
      }

      const cartItems = await getCartItemsService(cart.id, token);

      set({
        cart,
        cartItems,
        loading: false,
      });
    } catch (error) {
      set({
        error: error.response?.data?.error || 'No se pudo cargar el carrito.',
        loading: false,
      });
    }
  },

  createCart: async (userId, status) => {
    set({
      loading: true,
      error: null,
    });

    try {
      const token = useAuthStore.getState().accessToken;

      const response = await createCartService(userId, status, token);

      const cart = response.shopping_cart || response;

      set({
        cart,
        cartItems: [],
        loading: false,
      });

      return cart;
    } catch (error) {
      set({
        error: error.message,
        loading: false,
      });

      throw error;
    }
  },

  addProductToCart: async (user_id, productId, quantity) => {
    set({
      loading: true,
      error: null,
    });

    try {
      const token = useAuthStore.getState().accessToken;

      let cart = null;

      cart = await getCartService(user_id, token);

      if (!cart) {
        const response = await createCartService(user_id, 'active', token);

        cart = response.shopping_cart || response;
      }

      const cartItems = await getCartItemsService(cart.id, token);

      const item = cartItems.find((item) => item.product_id === productId);

      if (item) {
        const newQuantity = item.quantity + quantity;

        await updateCartItemService(cart.id, productId, newQuantity, token);
      } else {
        await addToCartService(cart.id, productId, quantity, token);
      }

      const updatedCartItems = await getCartItemsService(cart.id, token);

      set({
        cart,
        cartItems: updatedCartItems,
        loading: false,
      });
    } catch (error) {
      set({
        error:
          error.response?.data?.error ||
          'No se pudo agregar el producto al carrito.',
        loading: false,
      });

      throw error;
    }
  },

  deleteProductFromCart: async (cartId, productId) => {
    set({
      loading: true,
      error: null,
    });

    try {
      const token = useAuthStore.getState().accessToken;

      await removeFromCartService(cartId, productId, token);

      const cartItems = await getCartItemsService(cartId, token);

      if (cartItems.length === 0) {
        await deleteCartService(cartId, token);

        set({
          cart: null,
          cartItems: [],
          loading: false,
        });

        return;
      }

      set({
        cartItems,
        loading: false,
      });
    } catch (error) {
      set({
        error: error.message,
        loading: false,
      });

      throw error;
    }
  },

  deleteCart: async (cartId) => {
    set({
      loading: true,
      error: null,
    });

    try {
      const token = useAuthStore.getState().accessToken;

      await deleteCartService(cartId, token);

      set({
        cart: null,
        cartItems: [],
        loading: false,
      });
    } catch (error) {
      set({
        error: error.message,
        loading: false,
      });

      throw error;
    }
  },

  updateCartItem: async (cartId, productId, quantity) => {
    set({
      loading: true,
      error: null,
    });

    try {
      const token = useAuthStore.getState().accessToken;

      await updateCartItemService(cartId, productId, quantity, token);

      const cartItems = await getCartItemsService(cartId, token);
      console.log('Nuevos cartItems:', cartItems);
      set({
        cartItems,
        loading: false,
      });
    } catch (error) {
      set({
        error:
          error.response?.data?.error ||
          'No se pudo actualizar la cantidad del producto.',
        loading: false,
      });

      throw error;
    }
  },
}));
