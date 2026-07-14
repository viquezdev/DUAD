import products from '../../data/products.json';
import './ProductTable.css';

export const ProductTable = () => {
  return (
    <div className="tableContainer">
      <h1>Administración de productos</h1>
      <p>
        En esta sección puedes gestionar el catálogo de productos de PawStore
      </p>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>NOMBRE</th>
            <th>PRECIO</th>
            <th>CATEGORÍA</th>
            <th>STOCK</th>
            <th>ACCIONES</th>
          </tr>
        </thead>

        <tbody>
          {products.map((product) => (
            <tr key={product.id}>
              <td>{product.id}</td>
              <td>{product.nombre}</td>
              <td>₡ {product.precio}</td>
              <td className="productCategory">{product.categoria}</td>
              <td>{product.stock}</td>

              <td>
                <button className="btnEdit">Editar</button>

                <button className="btnDelete">Eliminar</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};
