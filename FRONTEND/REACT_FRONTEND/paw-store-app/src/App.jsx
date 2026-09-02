import { BrowserRouter, useRoutes } from 'react-router-dom';
import { Header } from './components/layout/Header';
import { Footer } from './components/layout/Footer';
import { routes } from './routes/routes';
import { AuthProvider } from './context/AuthProvider';
import { CartProvider } from './context/CartProvider';

const AppRoutes = () => {
  return useRoutes(routes);
};

function App() {
  return (
    <BrowserRouter>
      <AuthProvider>
        <CartProvider>
          <Header />

          <AppRoutes />

          <Footer />
        </CartProvider>
      </AuthProvider>
    </BrowserRouter>
  );
}

export default App;
