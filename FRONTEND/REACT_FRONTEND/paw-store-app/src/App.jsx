import { useState } from 'react';
import { Header } from './components/layout/header';
import './index.css';
import { Footer } from './components/layout/Footer';
import { Index } from './components/pages/Index';
import { Product } from './components/pages/Product';
import { Products } from './components/pages/Products';

function App() {
  const [page, setPage] = useState('home');
  return (
    <>
      <Header setPage={setPage} />
      {page === 'home' && <Index />}
      {page === 'products' && <Products />}
      {page === 'product' && <Product />}
      <Footer />
    </>
  );
}

export default App;
