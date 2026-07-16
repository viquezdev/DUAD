import './Product.css';
import { useProductStore } from '../store/productStore';

export const Product = ({ setPage }) => {
  const product = useProductStore((state) => state.selectedProduct);

  if (!product) {
    return (
      <div className="product-page">
        <h1>Detalle del producto</h1>

        <p>No hay ningún producto seleccionado.</p>

        <button className="btn-detail" onClick={() => setPage('products')}>
          Volver al catálogo
        </button>
      </div>
    );
  }
  return (
    <div className="product-page">
      <div className="detail-image-container">
        <img
          src={product.imagen}
          alt={product.nombre}
          className="detail-image"
        />
      </div>
      <div className="product-detail">
        <h1>{product.nombre}</h1>

        <p className="price-detail">₡ {product.precio}</p>
        <p>{product.categoria}</p>

        <p className="description">{product.descripcion}</p>

        <button
          className="btn-detail"
          onClick={() => {
            setPage('products');
          }}
        >
          Volver al catálogo
        </button>
      </div>
    </div>
  );
};
