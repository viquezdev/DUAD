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
      const cartItems = await getCartItemsService(cart.id, token);
      set({
        cart,
        cartItems,
        loading: false,
      });
    } catch (error) {
      set({
        error: error.message,
        loading: false,
      });
    }
  },
  createCart: async (userId, status, created_at) => {
    set({
      loading: true,
      error: null,
    });
    try {
      const token = useAuthStore.getState().accessToken;
      const cart = await createCartService(userId, status, created_at, token);
      set({
        cart,
        loading: false,
      });
    } catch (error) {
      set({
        error: error.message,
        loading: false,
      });
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
        set({ cart: null, cartItems: [] });
      }
      set({
        loading: false,
      });
    } catch (error) {
      set({
        error: error.message,
        loading: false,
      });
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
    }
  },

  addToCart: async (cartId, productId, quantity) => {
    set({
      loading: true,
      error: null,
    });
    try {
      const token = useAuthStore.getState().accessToken;
      await addToCartService(cartId, productId, quantity, token);
      const cartItems = await getCartItemsService(cartId, token);
      set({
        cartItems,
        loading: false,
      });
    } catch (error) {
      set({
        error: error.message,
        loading: false,
      });
    }
  },
}));
