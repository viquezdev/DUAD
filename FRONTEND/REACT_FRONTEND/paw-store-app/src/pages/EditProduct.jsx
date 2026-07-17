import { useProductStore } from '../store/productStore';
import { ProductForm } from '../components/ProductForm/ProductForm';
import './EditProduct.css';

export const EditProduct = ({ setPage }) => {
  const products = useProductStore((state) => state.products);
  const selectedProductId = useProductStore((state) => state.selectedProductId);
  const product = products.find((p) => p.id === selectedProductId);
  if (!product) {
    return (
      <div>
        <h1>Producto no encontrado</h1>
        <button className="btnAdmin" onClick={() => setPage('adminProducts')}>
          Volver a la administración
        </button>
      </div>
    );
  }
  return <ProductForm mode="edit" product={product} setPage={setPage} />;
};
