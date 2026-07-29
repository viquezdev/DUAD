import { create } from 'zustand';
import { getProducts } from '../services/productService';

export const useProductStore = create((set) => ({
  products: [],
  loading: false,
  error: null,
  selectedProductId: null,
  successMessage: '',

  loadProducts: async () => {
    set({
      loading: true,
      error: null,
    });

    try {
      const products = await getProducts();

      set({
        products,
        loading: false,
      });
    } catch (error) {
      console.error(error);

      set({
        loading: false,
        error: 'No se pudieron cargar los productos.',
      });
    }
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
