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
  const [selectedProduct, setSelectedProduct] = useState(null);
  return (
    <>
      <Header page={page} setPage={setPage} />
      {page === 'home' && <Home setPage={setPage} />}
      {page === 'products' && (
        <Products setPage={setPage} setSelectedProduct={setSelectedProduct} />
      )}
      {page === 'details' && (
        <Product product={selectedProduct} setPage={setPage} />
      )}
      {page === 'contact' && <Contact />}
      {page === 'adminProducts' && <ProductManagement setPage={setPage} />}
      {page === 'editProduct' && <EditProduct />}

      <Footer />
    </>
  );
}

export default App;
