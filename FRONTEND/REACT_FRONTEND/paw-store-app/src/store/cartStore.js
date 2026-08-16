import { create } from 'zustand';
import {
  getCartService,
  addToCartService,
  removeFromCartService,
  updateCartItemService,
  createCartService,
  getCartItemsService,
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
}));
