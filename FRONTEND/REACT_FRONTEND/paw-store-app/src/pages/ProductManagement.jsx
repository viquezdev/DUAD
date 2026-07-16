import './ProductManagement.css';
import { ProductTable } from '../components/ProductTable/ProductTable';
import { ProductForm } from '../components/ProductForm/ProductForm';
import { useProductStore } from '../store/productStore';
import { useEffect } from 'react';

export const ProductManagement = ({ setPage }) => {
  const successMessage = useProductStore((state) => state.successMessage);
  const clearSuccessMessage = useProductStore(
    (state) => state.clearSuccessMessage
  );

  useEffect(() => {
    if (!successMessage) return;

    const timer = setTimeout(() => {
      clearSuccessMessage();
    }, 3000);

    return () => clearTimeout(timer);
  }, [successMessage, clearSuccessMessage]);

  return (
    <main className="product-management">
      {successMessage && <div className="successMessage">{successMessage}</div>}
      <ProductTable setPage={setPage} />
      <ProductForm mode="create" setPage={setPage} />
    </main>
  );
};
