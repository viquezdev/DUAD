import './Home.css';

export const Home = ({ setPage }) => {
  return (
    <main>
      <div className="home-page">
        <h1>Bienvenido a PawStore</h1>
        <p>
          Somos una tienda dedicada a ofrecer productos de calidad para tus
          mascotas.
        </p>
        <p>
          Explora nuestro catálogo para encontrar camas, juguetes, accesorios y
          más.
        </p>
        <button className="btn-products" onClick={() => setPage('products')}>
          Ver productos
        </button>
        <p>
          Esta es la página principal de la aplicación. Más adelante aquí se
          podrán mostrar productos destacados.
        </p>
      </div>
    </main>
  );
};
