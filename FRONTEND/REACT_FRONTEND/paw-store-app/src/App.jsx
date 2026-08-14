import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { Header } from './components/layout/Header';
import { Footer } from './components/layout/Footer';
import { routes } from './routes/routes';

function App() {
  return (
    <BrowserRouter>
      <Header />

      <Routes>
        {routes.map((route) => (
          <Route key={route.path} path={route.path} element={route.element} />
        ))}
      </Routes>

      <Footer />
    </BrowserRouter>
  );
}

export default App;
