import { create } from 'zustand';

export const useAuthStore = create((set) => ({
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
}));
