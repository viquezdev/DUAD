import { Home } from '../pages/Home';
import { Products } from '../pages/Products';
import { Product } from '../pages/Product';
import { Contact } from '../pages/Contact';
import { Login } from '../pages/Login';
import { ProductManagement } from '../pages/ProductManagement';
import { EditProduct } from '../pages/EditProduct';
import { Cart } from '../pages/Cart';
import { Checkout } from '../pages/Checkout';
import { PurchaseSuccess } from '../pages/PurchaseSuccess';
import { NotFound } from '../pages/NotFound';
import { AdminRoute } from './AdminRoute';

export const routes = [
  {
    path: '/',
    element: <Home />,
  },
  {
    path: '/productos',
    element: <Products />,
  },
  {
    path: '/productos/:id',
    element: <Product />,
  },
  {
    path: '/contacto',
    element: <Contact />,
  },
  {
    path: '/login',
    element: <Login />,
  },
  {
    element: <AdminRoute />,
    children: [
      {
        path: '/admin',
        element: <ProductManagement />,
      },
      {
        path: '/admin/editar/:id',
        element: <EditProduct />,
      },
    ],
  },
  {
    path: '/carrito',
    element: <Cart />,
  },
  {
    path: '/checkout',
    element: <Checkout />,
  },
  {
    path: '/purchase-success',
    element: <PurchaseSuccess />,
  },
  {
    path: '*',
    element: <NotFound />,
  },
];
