import './ProductTable.css';
import { useProductStore } from '../../store/productStore';
import { useNavigate } from 'react-router-dom';
import { useEffect } from 'react';

export const ProductTable = () => {
  const loadProducts = useProductStore((state) => state.loadProducts);
  const products = useProductStore((state) => state.products);
  const deleteProduct = useProductStore((state) => state.deleteProduct);
  const navigate = useNavigate();

  useEffect(() => {
    if (products.length === 0) {
      loadProducts();
    }
  }, [products.length, loadProducts]);

  return (
    <div className="tableContainer">
      <h1>Administración de productos</h1>
      <p>
        En esta sección puedes gestionar el catálogo de productos de PawStore
      </p>
      <table>
        <caption>
          Lista de productos registrados en el catálogo de PawStore.
        </caption>

        <thead>
          <tr>
            <th scope="col">ID</th>
            <th scope="col">NOMBRE</th>
            <th scope="col">PRECIO</th>
            <th scope="col">CATEGORÍA</th>
            <th scope="col">STOCK</th>
            <th scope="col">ACCIONES</th>
          </tr>
        </thead>

        <tbody>
          {products.map((product) => (
            <tr key={product.id}>
              <td>{product.id}</td>
              <td>{product.name}</td>
              <td>₡ {product.price}</td>
              <td className="productCategory">{product.category}</td>
              <td>{product.quantity}</td>

              <td>
                <button
                  className="btnEdit"
                  aria-label={`Editar ${product.name}`}
                  onClick={() => {
                    navigate(`/admin/products/edit/${product.id}`);
                  }}
                >
                  Editar
                </button>

                <button
                  className="btnDelete"
                  aria-label={`Eliminar ${product.name}`}
                  onClick={() => deleteProduct(product.id)}
                >
                  Eliminar
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};
