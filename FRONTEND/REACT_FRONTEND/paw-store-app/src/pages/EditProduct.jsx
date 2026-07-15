import { useProductStore } from '../store/productStore';
import { ProductForm } from '../components/ProductForm/ProductForm';

export const EditProduct = ({ setPage }) => {
  const selectedProduct = useProductStore((state) => state.selectedProduct);
  return (
    <ProductForm mode="edit" product={selectedProduct} setPage={setPage} />
  );
};
