import './ProductCard.css';
import { useNavigate } from 'react-router-dom';

export const ProductCard = ({ product }) => {
  const navigate = useNavigate();

  const handleDetails = () => {
    navigate(`/productos/${product.id}`);
  };

  return (
    <article className="product-card">
      <div className="product-image-container">
        <img src={product.image} alt={product.name} className="product-image" />
      </div>

      <div className="product-content">
        <h2>{product.name}</h2>

        <p className="price">₡ {product.price}</p>

        <p>{product.category}</p>

        <button onClick={handleDetails}>Ver detalles</button>
      </div>
    </article>
  );
};
