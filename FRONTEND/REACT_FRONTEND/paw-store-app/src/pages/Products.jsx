import { useProductStore } from '../store/productStore';
import { ProductCard } from '../components/ProductCard/ProductCard';
import { useEffect } from 'react';
import './Products.css';
import { Loading } from '../components/Loading/Loading';

export const Products = () => {
  const loadProducts = useProductStore((state) => state.loadProducts);
  const products = useProductStore((state) => state.products);
  const error = useProductStore((state) => state.error);
  const loading = useProductStore((state) => state.loading);

  useEffect(() => {
    loadProducts();
  }, [loadProducts]);

  if (loading) {
    return <Loading />;
  }

  if (error) {
    return <p>{error}</p>;
  }

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
          <ProductCard key={product.id} product={product} />
        ))}
      </div>
    </div>
  );
};
