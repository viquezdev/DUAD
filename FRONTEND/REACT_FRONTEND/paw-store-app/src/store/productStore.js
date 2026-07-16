import { create } from 'zustand';
import productsData from '../data/products.json';

export const useProductStore = create((set) => ({
  products: productsData,
  selectedProduct: null,
  successMessage: '',

  addProduct: (newProduct) =>
    set((state) => {
      let newId;

      if (state.products.length > 0) {
        newId = Math.max(...state.products.map((p) => p.id)) + 1;
      } else {
        newId = 1;
      }

      const product = {
        id: newId,
        ...newProduct,
      };

      return {
        products: [...state.products, product],
      };
    }),

  deleteProduct: (id) =>
    set((state) => ({
      products: state.products.filter((product) => product.id !== id),
    })),

  updateProduct: (updatedProduct) =>
    set((state) => ({
      products: state.products.map((product) =>
        product.id === updatedProduct.id ? updatedProduct : product
      ),
    })),

  setSelectedProduct: (product) =>
    set({
      selectedProduct: product,
    }),

  clearSelectedProduct: () =>
    set({
      selectedProduct: null,
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
