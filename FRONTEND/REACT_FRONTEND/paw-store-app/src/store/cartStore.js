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

import { useInvoiceStore } from './invoiceStore';

export const selectCartTotal = (state) =>
  state.cartItems.reduce((total, item) => total + Number(item.subtotal), 0);

export const selectCartCount = (state) =>
  state.cartItems.reduce((total, item) => total + Number(item.quantity), 0);

export const useCartStore = create((set) => ({
  cart: null,
  cartItems: [],
  loading: false,
  error: null,
  checkoutEnabled: false,

  enableCheckout: () => {
    set({
      checkoutEnabled: true,
    });
  },

  disableCheckout: () => {
    set({
      checkoutEnabled: false,
    });
  },

  clearCart: () => {
    set({
      cart: null,
      cartItems: [],
    });
    useInvoiceStore.getState().clearInvoice();
    useCartStore.getState().disableCheckout();
  },

  loadCart: async (userId, accessToken) => {
    set({
      loading: true,
      error: null,
    });

    try {
      const cart = await getCartService(userId, accessToken);

      if (!cart) {
        set({
          cart: null,
          cartItems: [],
          loading: false,
        });

        return;
      }

      const cartItems = await getCartItemsService(cart.id, accessToken);

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

  createCart: async (userId, status, accessToken) => {
    set({
      loading: true,
      error: null,
    });

    try {
      const response = await createCartService(userId, status, accessToken);

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

  addProductToCart: async (user_id, productId, quantity, accessToken) => {
    set({
      loading: true,
      error: null,
    });

    try {
      let cart = null;

      cart = await getCartService(user_id, accessToken);

      if (!cart) {
        const response = await createCartService(
          user_id,
          'active',
          accessToken
        );

        cart = response.shopping_cart || response;
      }

      const cartItems = await getCartItemsService(cart.id, accessToken);

      const item = cartItems.find((item) => item.product_id === productId);

      if (item) {
        const newQuantity = item.quantity + quantity;

        await updateCartItemService(
          cart.id,
          productId,
          newQuantity,
          accessToken
        );
      } else {
        await addToCartService(cart.id, productId, quantity, accessToken);
      }

      const updatedCartItems = await getCartItemsService(cart.id, accessToken);

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

  deleteProductFromCart: async (cartId, productId, accessToken) => {
    set({
      loading: true,
      error: null,
    });

    try {
      await removeFromCartService(cartId, productId, accessToken);

      const cartItems = await getCartItemsService(cartId, accessToken);

      if (cartItems.length === 0) {
        await deleteCartService(cartId, accessToken);

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

  deleteCart: async (cartId, accessToken) => {
    set({
      loading: true,
      error: null,
    });

    try {
      await deleteCartService(cartId, accessToken);

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
      await updateCartItemService(cartId, productId, quantity, accessToken);

      const cartItems = await getCartItemsService(cartId, accessToken);
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
