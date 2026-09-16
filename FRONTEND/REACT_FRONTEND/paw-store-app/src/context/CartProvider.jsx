import { useState, useCallback } from 'react';
import { CartContext } from './CartContext';
import { useAuth } from './useAuth';

import {
  getCartService,
  addToCartService,
  removeFromCartService,
  updateCartItemService,
  createCartService,
  getCartItemsService,
  deleteCartService,
} from '../services/cartService';

export const CartProvider = ({ children }) => {
  const { accessToken } = useAuth();

  const [cart, setCart] = useState(null);
  const [cartItems, setCartItems] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [checkoutEnabled, setCheckoutEnabled] = useState(false);

  const clearCart = useCallback(() => {
    setCart(null);
    setCartItems([]);
    setCheckoutEnabled(false);
  }, []);

  const enableCheckout = useCallback(() => {
    setCheckoutEnabled(true);
  }, []);

  const disableCheckout = useCallback(() => {
    setCheckoutEnabled(false);
  }, []);

  const loadCart = useCallback(
    async (userId) => {
      setLoading(true);
      setError(null);

      try {
        const currentCart = await getCartService(userId, accessToken);

        if (!currentCart) {
          setCart(null);
          setCartItems([]);
          setLoading(false);
          return;
        }

        const currentCartItems = await getCartItemsService(
          currentCart.id,
          accessToken
        );

        setCart(currentCart);
        setCartItems(currentCartItems);
        setLoading(false);
      } catch (error) {
        setError(
          error.response?.data?.error || 'No se pudo cargar el carrito.'
        );
        setLoading(false);
      }
    },
    [accessToken]
  );

  const createCart = async (userId, status) => {
    setLoading(true);
    setError(null);

    try {
      const response = await createCartService(userId, status, accessToken);

      const newCart = response.shopping_cart || response;

      setCart(newCart);
      setCartItems([]);
      setLoading(false);

      return newCart;
    } catch (error) {
      setError(error.message);
      setLoading(false);

      throw error;
    }
  };

  const addProductToCart = async (userId, productId, quantity) => {
    setLoading(true);
    setError(null);

    try {
      let currentCart = await getCartService(userId, accessToken);

      if (!currentCart) {
        const response = await createCartService(userId, 'active', accessToken);

        currentCart = response.shopping_cart || response;
      }

      const currentCartItems = await getCartItemsService(
        currentCart.id,
        accessToken
      );

      const item = currentCartItems.find(
        (item) => item.product_id === productId
      );

      if (item) {
        const newQuantity = item.quantity + quantity;

        await updateCartItemService(
          currentCart.id,
          productId,
          newQuantity,
          accessToken
        );
      } else {
        await addToCartService(
          currentCart.id,
          productId,
          quantity,
          accessToken
        );
      }

      const updatedCartItems = await getCartItemsService(
        currentCart.id,
        accessToken
      );

      setCart(currentCart);
      setCartItems(updatedCartItems);
      setLoading(false);
    } catch (error) {
      setError(
        error.response?.data?.error ||
          'No se pudo agregar el producto al carrito.'
      );

      setLoading(false);

      throw error;
    }
  };

  const deleteProductFromCart = async (cartId, productId) => {
    setLoading(true);
    setError(null);

    try {
      await removeFromCartService(cartId, productId, accessToken);

      const updatedCartItems = await getCartItemsService(cartId, accessToken);

      if (updatedCartItems.length === 0) {
        await deleteCartService(cartId, accessToken);

        setCart(null);
        setCartItems([]);
        setLoading(false);

        return;
      }

      setCartItems(updatedCartItems);
      setLoading(false);
    } catch (error) {
      setError(error.message);
      setLoading(false);

      throw error;
    }
  };

  const deleteCart = async (cartId) => {
    setLoading(true);
    setError(null);

    try {
      await deleteCartService(cartId, accessToken);

      setCart(null);
      setCartItems([]);
      setLoading(false);
    } catch (error) {
      setError(error.message);
      setLoading(false);

      throw error;
    }
  };

  const updateCartItem = async (cartId, productId, quantity) => {
    setLoading(true);
    setError(null);

    try {
      await updateCartItemService(cartId, productId, quantity, accessToken);

      const updatedCartItems = await getCartItemsService(cartId, accessToken);

      console.log('Nuevos cartItems:', updatedCartItems);

      setCartItems(updatedCartItems);
      setLoading(false);
    } catch (error) {
      setError(
        error.response?.data?.error ||
          'No se pudo actualizar la cantidad del producto.'
      );

      setLoading(false);

      throw error;
    }
  };

  const cartTotal = cartItems.reduce(
    (total, item) => total + Number(item.subtotal),
    0
  );

  const cartCount = cartItems.reduce(
    (total, item) => total + Number(item.quantity),
    0
  );

  return (
    <CartContext.Provider
      value={{
        cart,
        cartItems,
        loading,
        error,
        checkoutEnabled,

        cartTotal,
        cartCount,

        enableCheckout,
        disableCheckout,
        clearCart,
        loadCart,
        createCart,
        addProductToCart,
        deleteProductFromCart,
        deleteCart,
        updateCartItem,
      }}
    >
      {children}
    </CartContext.Provider>
  );
};
