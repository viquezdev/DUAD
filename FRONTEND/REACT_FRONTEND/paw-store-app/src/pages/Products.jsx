import { useProductStore } from '../store/productStore';
import { ProductCard } from '../components/ProductCard/ProductCard';
import './Products.css';

export const Products = ({ setPage }) => {
  const products = useProductStore((state) => state.products);

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
          <ProductCard key={product.id} product={product} setPage={setPage} />
        ))}
      </div>
    </div>
  );
};
