import './ProductCard.css';
import { useProductStore } from '../../store/productStore';

export const ProductCard = ({ product, setPage }) => {
  const setSelectedProduct = useProductStore(
    (state) => state.setSelectedProduct
  );
  return (
    <article className="product-card">
      <div className="product-image-container">
        <img src={product.image} alt={product.name} className="product-image" />
      </div>

      <div className="product-content">
        <h2>{product.name}</h2>

        <p className="price">₡ {product.price}</p>

        <p>{product.category}</p>

        <button
          onClick={() => {
            setSelectedProduct(product.id);
            setPage('details');
          }}
        >
          Ver detalles
        </button>
      </div>
    </article>
  );
};
