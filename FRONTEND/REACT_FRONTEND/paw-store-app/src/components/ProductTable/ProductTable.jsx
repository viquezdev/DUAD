import './ProductTable.css';
import { useProductStore } from '../../store/productStore';

export const ProductTable = ({ setPage }) => {
  const products = useProductStore((state) => state.products);
  const deleteProduct = useProductStore((state) => state.deleteProduct);
  const setSelectedProduct = useProductStore(
    (state) => state.setSelectedProduct
  );
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
                    setSelectedProduct(product.id);
                    setPage('editProduct');
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
