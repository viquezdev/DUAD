import products from '../../data/products.json';
import { ProductCard } from '../ProductCard/ProductCard';
import './Products.css';

export const Products = () => {
  return (
    <div className="products-grid">
      {products.map((product) => (
        <ProductCard key={product.id} product={product} />
      ))}
    </div>
  );
};
