import './ProductCard.css';
import { useProductStore } from '../../store/productStore';

export const ProductCard = ({ product, setPage }) => {
  const setSelectedProduct = useProductStore(
    (state) => state.setSelectedProduct
  );
  return (
    <article className="product-card">
      <div className="product-image-container">
        <img
          src={product.imagen}
          alt={product.nombre}
          className="product-image"
        />
      </div>

      <div className="product-content">
        <h2>{product.nombre}</h2>

        <p className="price">₡ {product.precio}</p>

        <p>{product.categoria}</p>

        <button
          onClick={() => {
            setSelectedProduct(product);
            setPage('details');
          }}
        >
          Ver detalles
        </button>
      </div>
    </article>
  );
};
