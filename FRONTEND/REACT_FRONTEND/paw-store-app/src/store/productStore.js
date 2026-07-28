import { create } from 'zustand';
import { getProducts } from '../services/productService';

export const useProductStore = create((set) => ({
  products: [],
  loading: false,
  selectedProductId: null,
  successMessage: '',

  loadProducts: async () => {
    set({ loading: true });

    const products = await getProducts();

    set({
      products,
      loading: false,
    });
  },

  setSelectedProduct: (id) =>
    set({
      selectedProductId: id,
    }),

  clearSelectedProduct: () =>
    set({
      selectedProductId: null,
    }),

  setSuccessMessage: (message) =>
    set({
      successMessage: message,
    }),

  clearSuccessMessage: () =>
    set({
      successMessage: '',
    }),
}));
