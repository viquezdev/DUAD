import products from '../data/products.json';
import { ProductCard } from '../components/ProductCard/ProductCard';
import './Products.css';

export const Products = ({ setPage, setSelectedProduct }) => {
  if (products.length === 0) {
    return (
      <div className="empty-products">
        <img src="/images/stock-out.svg" className="empty-products-img" />
        <h2>No se encontraron productos</h2>
      </div>
    );
  }

  return (
    <div className="products-page">
      <h1>Catálogo de productos</h1>
      <div className="products-grid">
        {products.map((product) => (
          <ProductCard
            key={product.id}
            product={product}
            setPage={setPage}
            setSelectedProduct={setSelectedProduct}
          />
        ))}
      </div>
    </div>
  );
};
