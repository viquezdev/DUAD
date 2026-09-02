import { Link, NavLink } from 'react-router-dom';
import pawStoreLogo from '../../assets/pawStoreLogo.png';
import './Header.css';
import { useAuth } from '../../context/useAuth.js';
import { useCart } from '../../context/useCart.js';

export const Header = () => {
  const { user, logoutUser } = useAuth();

  const { checkoutEnabled, cartCount, clearCart } = useCart();

  return (
    <header>
      <nav className="navbar-container">
        <div className="nav-left">
          <Link to="/" className="nav-brand">
            <img src={pawStoreLogo} alt="PawStore" className="brand-image" />
            <span className="brand-name">PawStore</span>
          </Link>
        </div>

        <div className="nav-right">
          <NavLink
            to="/"
            className={({ isActive }) =>
              isActive ? 'nav-link active' : 'nav-link'
            }
          >
            Inicio
          </NavLink>
          <NavLink
            to="/products"
            className={({ isActive }) =>
              isActive ? 'nav-link active' : 'nav-link'
            }
          >
            Productos
          </NavLink>
          <NavLink
            to="/contact"
            className={({ isActive }) =>
              isActive ? 'nav-link active' : 'nav-link'
            }
          >
            Contacto
          </NavLink>
          <NavLink
            to="/cart"
            className={({ isActive }) =>
              isActive ? 'nav-link active' : 'nav-link'
            }
          >
            Carrito
            <span className="cart-count">{cartCount}</span>
          </NavLink>
          {checkoutEnabled && (
            <NavLink
              to="/checkout"
              className={({ isActive }) =>
                isActive ? 'nav-link active' : 'nav-link'
              }
            >
              Checkout
            </NavLink>
          )}
          <NavLink
            to="/admin/products"
            className={({ isActive }) =>
              isActive ? 'nav-link active' : 'nav-link'
            }
          >
            Administración
          </NavLink>
          {user ? (
            <>
              <div className="user-section">
                <span className="nav-user">
                  Sesión iniciada como: {user.username}
                </span>
                <NavLink
                  to="/"
                  className="btnLogout"
                  onClick={() => {
                    clearCart();
                    logoutUser();
                  }}
                >
                  Cerrar sesión
                </NavLink>
              </div>
            </>
          ) : (
            <NavLink
              to="/login"
              className={({ isActive }) =>
                isActive ? 'nav-link active' : 'nav-link'
              }
            >
              Iniciar sesión
            </NavLink>
          )}
        </div>
      </nav>
    </header>
  );
};
