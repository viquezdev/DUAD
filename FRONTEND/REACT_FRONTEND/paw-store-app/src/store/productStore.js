import { create } from 'zustand';
import { getProducts, addProduct } from '../services/productService';
import { useAuthStore } from '../store/authStore';

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

  createProduct: async (product) => {
    set({
      loading: true,
      error: null,
    });

    try {
      const token = useAuthStore.getState().accessToken;
      await addProduct(product, token);

      const products = await getProducts();

      set({
        products,
        loading: false,
        successMessage: 'Producto agregado correctamente',
      });
    } catch (error) {
      console.error(error);

      set({
        loading: false,
        error: 'No se pudo agregar el producto.',
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
