import pawStoreLogo from '../../assets/pawStoreLogo.png';
import './Header.css';

export const Header = ({ setPage }) => {
  return (
    <header>
      <nav className="navbar-container">
        <div className="nav-left">
          <a href="/" className="nav-brand">
            <img src={pawStoreLogo} alt="PawStore" className="brand-image" />
            <span className="brand-name">PawStore</span>
          </a>
        </div>

        <div className="nav-right">
          <button className="nav-link" onClick={() => setPage('home')}>
            Inicio
          </button>

          <button className="nav-link" onClick={() => setPage('products')}>
            Productos
          </button>

          <button className="nav-link">Contacto</button>
        </div>
      </nav>
    </header>
  );
};
