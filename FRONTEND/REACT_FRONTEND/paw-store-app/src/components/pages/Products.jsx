import products from '../../data/products.json';
import { ProductCard } from '../ProductCard/ProductCard';
import './Products.css';
import { useEffect, useState } from 'react';

export const Products = ({ setPage, setSelectedProduct }) => {
  const [loading, setLoading] = useState(true);
  useEffect(() => {
    const timer = setTimeout(() => {
      setLoading(false);
    }, 1500);

    return () => clearTimeout(timer);
  }, []);
  if (loading) {
    return (
      <div className="loading">
        <div className="spinner"></div>
        <p>Cargando productos...</p>
      </div>
    );
  }

  if (products.length === 0) {
    return (
      <div className="empty-products">
        <img src="/images/stock-out.svg" class="empty-products-img" />
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
