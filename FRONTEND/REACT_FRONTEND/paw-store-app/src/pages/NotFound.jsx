import { useNavigate } from 'react-router-dom';
import './NotFound.css';

export const NotFound = () => {
  const navigate = useNavigate();

  return (
    <div className="not-found">
      <h1>Página no encontrada</h1>

      <p>La ruta solicitada no existe o ha sido movida.</p>

      <button className="btn-not-found" onClick={() => navigate('/')}>
        Volver al inicio
      </button>
    </div>
  );
};
