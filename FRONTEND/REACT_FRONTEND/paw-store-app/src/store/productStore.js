import { create } from 'zustand';
import {
  getProducts,
  createProductService,
  updateProductService,
  deleteProductService,
} from '../services/productService';

export const useProductStore = create((set) => ({
  products: [],
  loading: false,
  error: null,
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

  createProduct: async (product, token) => {
    set({
      loading: true,
      error: null,
    });

    try {
      await createProductService(product, token);

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
      throw error;
    }
  },

  updateProduct: async (product, token) => {
    set({
      loading: true,
      error: null,
    });

    try {
      await updateProductService(product.id, product, token);

      const products = await getProducts();

      set({
        products,
        loading: false,
        successMessage: 'Producto actualizado correctamente',
      });
    } catch (error) {
      console.error(error);

      set({
        loading: false,
        error: 'No se pudo actualizar el producto.',
      });
      throw error;
    }
  },

  deleteProduct: async (id, token) => {
    set({
      loading: true,
      error: null,
    });

    try {
      await deleteProductService(id, token);

      const products = await getProducts();

      set({
        products,
        loading: false,
        successMessage: 'Producto eliminado correctamente',
      });
    } catch (error) {
      console.error(error);

      set({
        loading: false,
        error: 'No se pudo eliminar el producto.',
      });
      throw error;
    }
  },

  setSuccessMessage: (message) =>
    set({
      successMessage: message,
    }),

  clearSuccessMessage: () =>
    set({
      successMessage: '',
    }),
}));
