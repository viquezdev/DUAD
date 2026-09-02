import { useState } from 'react';
import { AuthContext } from './AuthContext';

const getInitialAuth = () => {
  const savedAuth = localStorage.getItem('pawstore-auth');

  if (!savedAuth) {
    return {
      user: null,
      accessToken: null,
      refreshToken: null,
      authMessage: '',
    };
  }

  try {
    const parsedAuth = JSON.parse(savedAuth);

    return {
      user: parsedAuth.state?.user || null,
      accessToken: parsedAuth.state?.accessToken || null,
      refreshToken: parsedAuth.state?.refreshToken || null,
      authMessage: parsedAuth.state?.authMessage || '',
    };
  } catch (error) {
    console.error('Error al recuperar la sesión:', error);

    localStorage.removeItem('pawstore-auth');

    return {
      user: null,
      accessToken: null,
      refreshToken: null,
      authMessage: '',
    };
  }
};

export const AuthProvider = ({ children }) => {
  const initialAuth = getInitialAuth();

  const [user, setUser] = useState(initialAuth.user);
  const [accessToken, setAccessToken] = useState(initialAuth.accessToken);
  const [refreshToken, setRefreshToken] = useState(initialAuth.refreshToken);
  const [authMessage, setAuthMessage] = useState(initialAuth.authMessage);
  const loginUser = (user, accessToken, refreshToken) => {
    setUser(user);
    setAccessToken(accessToken);
    setRefreshToken(refreshToken);

    localStorage.setItem(
      'pawstore-auth',
      JSON.stringify({
        state: {
          user,
          accessToken,
          refreshToken,
          authMessage,
        },
      })
    );
  };

  const logoutUser = () => {
    setUser(null);
    setAccessToken(null);
    setRefreshToken(null);
    setAuthMessage('');

    localStorage.removeItem('pawstore-auth');
  };

  const updateAuthMessage = (message) => {
    setAuthMessage(message);
  };

  const clearAuthMessage = () => {
    setAuthMessage('');
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        accessToken,
        refreshToken,
        authMessage,
        loginUser,
        logoutUser,
        updateAuthMessage,
        clearAuthMessage,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};
