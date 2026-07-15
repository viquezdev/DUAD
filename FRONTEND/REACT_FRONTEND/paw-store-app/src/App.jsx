import { useState } from 'react';
import { Header } from './components/layout/Header';
import { Footer } from './components/layout/Footer';
import { Home } from './pages/Home';
import { Product } from './pages/Product';
import { Products } from './pages/Products';
import { Contact } from './pages/Contact';
import { ProductManagement } from './pages/ProductManagement';
import { EditProduct } from './pages/EditProduct';

function App() {
  const [page, setPage] = useState('home');

  return (
    <>
      <Header page={page} setPage={setPage} />
      {page === 'home' && <Home setPage={setPage} />}
      {page === 'products' && <Products setPage={setPage} />}
      {page === 'details' && <Product setPage={setPage} />}
      {page === 'contact' && <Contact />}
      {page === 'adminProducts' && <ProductManagement setPage={setPage} />}
      {page === 'editProduct' && <EditProduct setPage={setPage} />}

      <Footer />
    </>
  );
}

export default App;
