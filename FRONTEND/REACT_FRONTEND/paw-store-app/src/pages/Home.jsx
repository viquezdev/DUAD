import { useAuth } from '../context/useAuth.js';
import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import './Home.css';

export const Home = () => {
  const { authMessage, clearAuthMessage } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    if (!authMessage) return;

    const timer = setTimeout(() => {
      clearAuthMessage();
    }, 3000);

    return () => clearTimeout(timer);
  }, [authMessage, clearAuthMessage]);
  return (
    <main>
      {authMessage && <div className="errorMessage">{authMessage}</div>}
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
        <button className="btn-products" onClick={() => navigate('/products')}>
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
