import './ProductManagement.css';
import { ProductTable } from '../components/ProductTable/ProductTable';
import { ProductForm } from '../components/ProductForm/ProductForm';

export const ProductManagement = ({ setPage }) => {
  return (
    <main className="product-management">
      <ProductTable setPage={setPage} />
      <ProductForm mode="create" setPage={setPage} />
    </main>
  );
};
