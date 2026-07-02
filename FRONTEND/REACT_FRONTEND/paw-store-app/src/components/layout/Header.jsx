import pawStoreLogo from '../../assets/pawStoreLogo.png';
import './Header.css';

export const Header = ({ page, setPage }) => {
  return (
    <header>
      <nav className="navbar-container">
        <div className="nav-left">
          <button className="nav-brand" onClick={() => setPage('home')}>
            <img src={pawStoreLogo} alt="PawStore" className="brand-image" />
            <span className="brand-name">PawStore</span>
          </button>
        </div>

        <div className="nav-right">
          <button
            className={page === 'home' ? 'nav-link active' : 'nav-link'}
            onClick={() => setPage('home')}
          >
            Inicio
          </button>

          <button
            className={
              page === 'products' || page === 'details'
                ? 'nav-link active'
                : 'nav-link'
            }
            onClick={() => setPage('products')}
          >
            Productos
          </button>

          <button
            className={page === 'contact' ? 'nav-link active' : 'nav-link'}
            onClick={() => setPage('contact')}
          >
            Contacto
          </button>
        </div>
      </nav>
    </header>
  );
};
