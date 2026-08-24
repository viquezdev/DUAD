import { Home } from '../pages/Home';
import { Products } from '../pages/Products';
import { Product } from '../pages/Product';
import { Contact } from '../pages/Contact';
import { Login } from '../pages/Login';
import { ProductManagement } from '../pages/ProductManagement';
import { EditProduct } from '../pages/EditProduct';
import { Cart } from '../pages/Cart';
import { Checkout } from '../pages/Checkout';

export const routes = [
  {
    path: '/',
    element: <Home />,
  },
  {
    path: '/products',
    element: <Products />,
  },
  {
    path: '/products/:id',
    element: <Product />,
  },
  {
    path: '/contact',
    element: <Contact />,
  },
  {
    path: '/login',
    element: <Login />,
  },
  {
    path: '/admin/products',
    element: <ProductManagement />,
  },
  {
    path: '/admin/products/edit/:id',
    element: <EditProduct />,
  },
  {
    path: '/cart',
    element: <Cart />,
  },
  {
    path: '/checkout',
    element: <Checkout />,
  },
];
