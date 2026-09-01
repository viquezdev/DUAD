import { Navigate, Outlet } from 'react-router-dom';
import { useAuthStore } from '../store/authStore';

export const AdminRoute = () => {
  const user = useAuthStore((state) => state.user);
  const setAuthMessage = useAuthStore((state) => state.setAuthMessage);

  if (!user) {
    return <Navigate to="/login" replace />;
  }

  if (!user.is_admin) {
    setAuthMessage('No tienes permiso para acceder a esta sección.');
    return <Navigate to="/" replace />;
  }

  return <Outlet />;
};
