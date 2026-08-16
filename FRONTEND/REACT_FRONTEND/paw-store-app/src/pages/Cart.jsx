import './Cart.css';
import { useCartStore } from '../store/cartStore';
import { useNavigate } from 'react-router-dom';
import { useAuthStore } from '../store/authStore';
import { useEffect } from 'react';

export const Cart = () => {
  const user = useAuthStore((state) => state.user);
  const cart = useCartStore((state) => state.cart);
  const cartItems = useCartStore((state) => state.cartItems);
  const navigate = useNavigate();
  useEffect(() => {
    if (!user) {
      navigate('/login');
    } else if (user && !cart) {
      useCartStore.getState().loadCart(user.id);
    }
  }, [user, navigate, cart]);

  return (
    <div className="cart-page">
      <h1>Carrito de compras</h1>
      {cartItems.length === 0 ? (
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
      ) : (
        <ul>
          {cartItems.map((item) => (
            <li key={item.id}>
              <span>{item.name}</span>
              <span>₡ {item.price}</span>
              <span>Cantidad: {item.quantity}</span>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};
