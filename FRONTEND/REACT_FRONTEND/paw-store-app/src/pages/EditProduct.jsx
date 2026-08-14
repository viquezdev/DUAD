import { useProductStore } from '../store/productStore';
import { ProductForm } from '../components/ProductForm/ProductForm';
import { useAuthStore } from '../store/authStore';
import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import './EditProduct.css';

export const EditProduct = () => {
  const user = useAuthStore((state) => state.user);
  const products = useProductStore((state) => state.products);
  const selectedProductId = useProductStore((state) => state.selectedProductId);
  const product = products.find((p) => p.id === selectedProductId);
  const navigate = useNavigate();
  useEffect(() => {
    if (!user || !user.is_admin) {
      navigate('/');
    }
  }, [user, navigate]);

  if (!user || !user.is_admin) {
    return null;
  }
  if (!product) {
    return (
      <div>
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
