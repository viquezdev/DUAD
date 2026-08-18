import './Cart.css';
import { useCartStore } from '../store/cartStore';
import { useNavigate } from 'react-router-dom';
import { useAuthStore } from '../store/authStore';
import { useEffect } from 'react';
import { useProductStore } from '../store/productStore';

export const Cart = () => {
  const user = useAuthStore((state) => state.user);

  const loadCart = useCartStore((state) => state.loadCart);
  const cartItems = useCartStore((state) => state.cartItems);

  const products = useProductStore((state) => state.products);
  const cart = useCartStore((state) => state.cart);

  const deleteProductFromCart = useCartStore(
    (state) => state.deleteProductFromCart
  );

  const navigate = useNavigate();

  useEffect(() => {
    if (!user) {
      navigate('/login');
      return;
    }

    loadCart(user.id);
  }, [user, navigate, loadCart]);

  return (
    <div className="cart-page">
      <h1>Carrito de compras</h1>

      {!cart ? (
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
        <>
          <div className="cart-container">
            <ul>
              {cartItems.map((item) => {
                const product = products.find(
                  (product) => product.id === item.product_id
                );

                if (!product) {
                  return null;
                }

                return (
                  <li key={item.product_id}>
                    <div className="cart-item-details">
                      <img className="cart-item-image" src={product.image} />
                      <h3>{product.name}</h3>

                      {/* <button
                        className="btn-quantity"
                        onClick={() => {
                          // Lógica para aumentar la cantidad
                        }}
                      >
                        -
                      </button>
                      <input type="number" min="1" value={item.quantity} />
                      <button
                        className="btn-quantity"
                        onClick={() => {
                          // Lógica para disminuir la cantidad
                        }}
                      >
                        +
                      </button> */}
                      <div>
                        <p>Precio: ₡ {product.price}</p>
                        <p className="subtotal">Subtotal: ₡ {item.subtotal}</p>
                      </div>

                      <button
                        className="btn-remove"
                        onClick={() => {
                          deleteProductFromCart(cart.id, item.product_id);
                        }}
                      >
                        Eliminar
                      </button>
                    </div>
                  </li>
                );
              })}
            </ul>
            <div className="cart-checkout">
              <h2>
                Total: ₡{' '}
                {cartItems.reduce((total, item) => total + item.subtotal, 0)}
              </h2>
              <button
                className="btn-checkout"
                onClick={() => {
                  // Lógica para proceder al pago
                }}
              >
                Continuar al checkout
              </button>
            </div>
          </div>
        </>
      )}
    </div>
  );
};
