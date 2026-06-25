import React from 'react';
import pawStoreLogo from '../../assets/pawStoreLogo.png';

export const Header = () => {
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
          <a href="/">Inicio</a>
          <a href="/productos">Productos</a>
          <a href="/contacto">Contacto</a>
        </div>
      </nav>
    </header>
  );
};
