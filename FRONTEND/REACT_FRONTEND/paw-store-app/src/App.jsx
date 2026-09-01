import { BrowserRouter, useRoutes } from 'react-router-dom';
import { Header } from './components/layout/Header';
import { Footer } from './components/layout/Footer';
import { routes } from './routes/routes';

const AppRoutes = () => {
  return useRoutes(routes);
};

function App() {
  return (
    <BrowserRouter>
      <Header />

      <AppRoutes />

      <Footer />
    </BrowserRouter>
  );
}

export default App;
