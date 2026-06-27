import products from '../../data/products.json';
import { ProductCard } from '../ProductCard/ProductCard';
import './Products.css';

export const Products = ({ setPage, setSelectedProduct }) => {
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
