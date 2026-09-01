import { useProductStore } from '../store/productStore';
import { ProductForm } from '../components/ProductForm/ProductForm';
import { useEffect } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import './EditProduct.css';

export const EditProduct = () => {
  const { id } = useParams();
  const navigate = useNavigate();

  const loading = useProductStore((state) => state.loading);
  const loadProducts = useProductStore((state) => state.loadProducts);
  const products = useProductStore((state) => state.products);

  useEffect(() => {
    loadProducts();
  }, [loadProducts]);

  if (loading) {
    return <h1>Cargando producto...</h1>;
  }

  const product = products.find((p) => p.id === Number(id));

  if (!product) {
    return (
      <div className="product-not-found">
        <h1>Producto no encontrado</h1>

        <button
          className="btnAdmin"
          onClick={() => navigate('/admin/products')}
        >
          Volver a la administración
        </button>
      </div>
    );
  }

  return <ProductForm mode="edit" product={product} />;
};
