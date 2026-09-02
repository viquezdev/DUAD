import './Cart.css';

import { useProductStore } from '../store/productStore';
import { useCart } from '../context/useCart.js';
import { useAuth } from '../context/useAuth.js';
import { useNavigate } from 'react-router-dom';
import { useEffect } from 'react';

export const Cart = () => {
  const { user } = useAuth();
  const {
    cart,
    cartItems,
    loadCart,
    updateCartItem,
    deleteProductFromCart,
    enableCheckout,
    cartTotal,
  } = useCart();
  const products = useProductStore((state) => state.products);

  const navigate = useNavigate();

  useEffect(() => {
    if (!user) {
      navigate('/login');
      return;
    }

    loadCart(user.id);
  }, [user, navigate, loadCart]);

  const handleAddQuantity = async (productId) => {
    console.log('productId:', productId);
    if (!cart) return;

    const item = cartItems.find((item) => item.product_id === productId);

    const product = products.find((product) => product.id === productId);

    if (!item || !product) return;

    if (item.quantity >= product.quantity) {
      return;
    }

    const newQuantity = item.quantity + 1;

    await updateCartItem(cart.id, productId, newQuantity);
  };

  const handleSubtractQuantity = async (productId) => {
    if (!cart) return;

    const item = cartItems.find((item) => item.product_id === productId);

    if (!item) return;

    if (item.quantity <= 1) {
      return;
    }

    const newQuantity = item.quantity - 1;

    await updateCartItem(cart.id, productId, newQuantity);
  };

  const handleDeleteProduct = async (productId) => {
    if (!cart) return;

    await deleteProductFromCart(cart.id, productId);
  };

  if (!cart) {
    return (
      <div className="cart-page">
        <h1>Carrito de compras</h1>

        <div className="empty-cart">
          <img
            src="/images/carrito.png"
            alt="Carrito vacío"
            className="empty-cart-image"
          />

          <h2>Tu carrito está vacío</h2>

          <p>Agrega productos para verlos aquí.</p>

          <button className="btn-back" onClick={() => navigate('/products')}>
            Ir a productos
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="cart-page">
      <h1>Carrito de compras</h1>

      <div className="cart-container">
        <ul>
          {cartItems.map((item) => {
            const product = products.find(
              (product) => product.id === item.product_id
            );

            if (!product) {
              return null;
            }

            const isMaxStock = item.quantity >= product.quantity;

            return (
              <li key={item.product_id}>
                <div className="cart-item-details">
                  <img
                    className="cart-item-image"
                    src={product.image}
                    alt={product.name}
                  />

                  <h3>{product.name}</h3>

                  <button
                    className="btn-quantity"
                    onClick={() => handleSubtractQuantity(item.product_id)}
                    disabled={item.quantity <= 1}
                    aria-label={`Disminuir cantidad de ${product.name}`}
                  >
                    -
                  </button>

                  <input
                    type="number"
                    min="1"
                    max={product.quantity}
                    value={item.quantity}
                    readOnly
                    aria-label={`Cantidad de ${product.name}`}
                  />

                  <button
                    className="btn-quantity"
                    onClick={() => handleAddQuantity(item.product_id)}
                    disabled={isMaxStock}
                    aria-label={`Aumentar cantidad de ${product.name}`}
                  >
                    +
                  </button>

                  <div>
                    <p>Precio: ₡ {product.price}</p>

                    <p className="subtotal">Subtotal: ₡ {item.subtotal}</p>

                    {isMaxStock && (
                      <small>No hay más unidades disponibles.</small>
                    )}
                  </div>

                  <button
                    className="btn-remove"
                    onClick={() => handleDeleteProduct(item.product_id)}
                  >
                    Quitar
                  </button>
                </div>
              </li>
            );
          })}
        </ul>

        <div className="cart-checkout">
          <h2>Total: ₡ {cartTotal}</h2>

          <button
            className="btn-checkout"
            onClick={() => {
              enableCheckout();
              navigate('/checkout');
            }}
          >
            Ir al checkout
          </button>
        </div>
      </div>
    </div>
  );
};
