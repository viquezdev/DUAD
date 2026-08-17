import './Product.css';
import { useProductStore } from '../store/productStore';
import { useCartStore } from '../store/cartStore';
import { useAuthStore } from '../store/authStore';
import { useNavigate } from 'react-router-dom';

export const Product = () => {
  const products = useProductStore((state) => state.products);

  const selectedProductId = useProductStore((state) => state.selectedProductId);

  const product = products.find((p) => p.id === selectedProductId);
  const navigate = useNavigate();

  if (!product) {
    return (
      <div className="product-page">
        <h1>Detalle del producto</h1>

        <p>No hay ningún producto seleccionado.</p>

        <button className="btn-detail" onClick={() => navigate('/products')}>
          Volver al catálogo
        </button>
      </div>
    );
  }
  return (
    <div className="product-page">
      <div className="detail-image-container">
        <img src={product.image} alt={product.name} className="detail-image" />
      </div>
      <div className="product-detail">
        <h1>{product.name}</h1>

        <p className="price-detail">₡ {product.price}</p>
        <p>{product.category}</p>

        <p className="description">{product.description}</p>

        <button
          className="btn-add-cart"
          onClick={() => {
            useCartStore.getState().loadCart(useAuthStore.getState().user.id);
            if (useCartStore.getState().cart) {
              useCartStore
                .getState()
                .addToCart(useCartStore.getState().cart.id, product.id, 1);
            } else {
              useCartStore
                .getState()
                .createCart(
                  useAuthStore.getState().user.id,
                  'active',
                  new Date().toISOString()
                );
            }

            navigate('/cart');
          }}
        >
          Agregar al carrito
        </button>

        <button
          className="btn-detail"
          onClick={() => {
            navigate('/products');
          }}
        >
          Volver al catálogo
        </button>
      </div>
    </div>
  );
};
