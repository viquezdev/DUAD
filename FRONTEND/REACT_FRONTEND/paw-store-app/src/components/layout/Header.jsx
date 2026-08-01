import pawStoreLogo from '../../assets/pawStoreLogo.png';
import './Header.css';
import { useAuthStore } from '../../store/authStore';

export const Header = ({ page, setPage }) => {
  const user = useAuthStore((state) => state.user);
  const logout = useAuthStore((state) => state.logout);
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
          <button
            className={
              page === 'adminProducts' || page === 'editProduct'
                ? 'nav-link active'
                : 'nav-link'
            }
            onClick={() => setPage('adminProducts')}
          >
            Administración
          </button>
          {user ? (
            <>
              <div className="user-section">
                <span className="nav-user">
                  Sesión iniciada como: {user.username}
                </span>

                <button
                  className="btnLogout"
                  onClick={() => {
                    logout();
                    setPage('home');
                  }}
                >
                  Cerrar sesión
                </button>
              </div>
            </>
          ) : (
            <button
              className={page === 'login' ? 'nav-link active' : 'nav-link'}
              onClick={() => setPage('login')}
            >
              Iniciar sesión
            </button>
          )}
        </div>
      </nav>
    </header>
  );
};
