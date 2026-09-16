import './Product.css';
import { useProductStore } from '../store/productStore';
import { useAuth } from '../context/useAuth';
import { useNavigate, useParams } from 'react-router-dom';
import { useEffect } from 'react';
import { useCart } from '../context/useCart';

export const Product = () => {
  const loadProducts = useProductStore((state) => state.loadProducts);
  const products = useProductStore((state) => state.products);

  const { addProductToCart } = useCart();
  const loading = useProductStore((state) => state.loading);
  const { user, accessToken } = useAuth();

  const navigate = useNavigate();

  const { id } = useParams();

  const product = products.find((p) => p.id === Number(id));

  useEffect(() => {
    if (products.length === 0) {
      loadProducts();
    }
  }, [products.length, loadProducts]);

  if (loading) {
    return <h1>Cargando producto...</h1>;
  }

  if (!product) {
    return (
      <div className="product-not-found">
        <h1>Producto no encontrado</h1>

        <p>Lo sentimos, no pudimos encontrar el producto que estás buscando.</p>

        <button className="btn-detail" onClick={() => navigate('/productos')}>
          Volver al catálogo
        </button>
      </div>
    );
  }

  const handleAddToCart = async () => {
    try {
      if (!user) {
        navigate('/login');
      } else {
        await addProductToCart(user.id, product.id, 1, accessToken);
        navigate('/carrito');
      }
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

        <button className="btn-detail" onClick={() => navigate('/productos')}>
          Volver al catálogo
        </button>
      </div>
    </div>
  );
};
