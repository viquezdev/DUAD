import { useState } from 'react';
import { Header } from './components/layout/header';
import './index.css';
import { Footer } from './components/layout/Footer';
import { Home } from './components/pages/Home';
import { Product } from './components/pages/Product';
import { Products } from './components/pages/Products';

function App() {
  const [page, setPage] = useState('home');
  const [selectedProduct, setSelectedProduct] = useState(null);
  return (
    <>
      <Header setPage={setPage} />
      {page === 'home' && <Home setPage={setPage} />}
      {page === 'products' && (
        <Products setPage={setPage} setSelectedProduct={setSelectedProduct} />
      )}
      {page === 'details' && (
        <Product product={selectedProduct} setPage={setPage} />
      )}
      <Footer />
    </>
  );
}

export default App;
