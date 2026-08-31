import { create } from 'zustand';
import { persist } from 'zustand/middleware';

export const useAuthStore = create(
  persist(
    (set) => ({
      user: null,
      accessToken: null,
      refreshToken: null,
      authMessage: '',

      login: (user, accessToken, refreshToken) =>
        set({
          user,
          accessToken,
          refreshToken,
        }),

      logout: () =>
        set({
          user: null,
          accessToken: null,
          refreshToken: null,
        }),

      setAuthMessage: (message) =>
        set({
          authMessage: message,
        }),

      clearAuthMessage: () =>
        set({
          authMessage: '',
        }),
    }),
    {
      name: 'pawstore-auth',
    }
  )
);
