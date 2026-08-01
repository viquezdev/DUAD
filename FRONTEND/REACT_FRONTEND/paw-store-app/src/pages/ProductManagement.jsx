import './ProductManagement.css';
import { ProductTable } from '../components/ProductTable/ProductTable';
import { ProductForm } from '../components/ProductForm/ProductForm';
import { useProductStore } from '../store/productStore';
import { useAuthStore } from '../store/authStore';
import { useEffect } from 'react';

export const ProductManagement = ({ setPage }) => {
  const user = useAuthStore((state) => state.user);
  const successMessage = useProductStore((state) => state.successMessage);
  const clearSuccessMessage = useProductStore(
    (state) => state.clearSuccessMessage
  );
  const setAuthMessage = useAuthStore((state) => state.setAuthMessage);

  useEffect(() => {
    if (!user || !user.is_admin) {
      setAuthMessage('No tienes permiso para acceder a esta sección.');
      setPage('home');
    }
  }, [user, setPage, setAuthMessage]);

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
      <ProductTable setPage={setPage} />
      <ProductForm mode="create" setPage={setPage} />
    </main>
  );
};
