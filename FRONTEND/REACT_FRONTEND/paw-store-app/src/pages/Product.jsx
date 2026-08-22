import './Product.css';
import { useProductStore } from '../store/productStore';
import { useCartStore } from '../store/cartStore';
import { useAuthStore } from '../store/authStore';
import { useNavigate } from 'react-router-dom';

export const Product = () => {
  const products = useProductStore((state) => state.products);
  const selectedProductId = useProductStore((state) => state.selectedProductId);

  const addProductToCart = useCartStore((state) => state.addProductToCart);

  const user = useAuthStore((state) => state.user);

  const navigate = useNavigate();

  const product = products.find((p) => p.id === selectedProductId);

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

  const handleAddToCart = async () => {
    try {
      await addProductToCart(user.id, product.id, 1);
      navigate('/cart');
    } catch (error) {
      console.error('Error al agregar producto al carrito:', error);
    }
  };

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
          onClick={handleAddToCart}
          disabled={product.quantity <= 0}
        >
          Agregar al carrito
        </button>

        {product.quantity <= 0 && (
          <small className="stock-message">No hay stock disponible</small>
        )}

        <button className="btn-detail" onClick={() => navigate('/products')}>
          Volver al catálogo
        </button>
      </div>
    </div>
  );
};
