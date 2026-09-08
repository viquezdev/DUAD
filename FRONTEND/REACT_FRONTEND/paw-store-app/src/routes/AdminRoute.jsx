import { Navigate, Outlet } from 'react-router-dom';
import { useAuth } from '../context/useAuth';

export const AdminRoute = () => {
  const { user } = useAuth();
  const { updateAuthMessage } = useAuth();

  if (!user) {
    return <Navigate to="/login" replace />;
  }

  if (!user.is_admin) {
    updateAuthMessage('No tienes permiso para acceder a esta sección.');
    return <Navigate to="/" replace />;
  }

  return <Outlet />;
};
