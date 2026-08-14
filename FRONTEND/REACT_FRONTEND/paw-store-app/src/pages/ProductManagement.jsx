import './ProductManagement.css';
import { ProductTable } from '../components/ProductTable/ProductTable';
import { ProductForm } from '../components/ProductForm/ProductForm';
import { useProductStore } from '../store/productStore';
import { useAuthStore } from '../store/authStore';
import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

export const ProductManagement = () => {
  const user = useAuthStore((state) => state.user);
  const successMessage = useProductStore((state) => state.successMessage);
  const clearSuccessMessage = useProductStore(
    (state) => state.clearSuccessMessage
  );
  const setAuthMessage = useAuthStore((state) => state.setAuthMessage);
  const navigate = useNavigate();

  useEffect(() => {
    if (!user || !user.is_admin) {
      setAuthMessage('No tienes permiso para acceder a esta sección.');
      navigate('/');
    }
  }, [user, navigate, setAuthMessage]);

  useEffect(() => {
    if (!successMessage) return;

    const timer = setTimeout(() => {
      clearSuccessMessage();
    }, 3000);

    return () => clearTimeout(timer);
  }, [successMessage, clearSuccessMessage]);

  if (!user || !user.is_admin) {
    return null;
  }

  return (
    <main className="product-management">
      {successMessage && <div className="successMessage">{successMessage}</div>}
      <ProductTable />
      <ProductForm mode="create" />
    </main>
  );
};
