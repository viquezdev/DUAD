import { create } from 'zustand';
import { createInvoiceService } from '../services/invoiceService';
import { useAuthStore } from './authStore';

export const useInvoiceStore = create((set) => ({
  invoice: null,
  loading: false,
  error: null,

  createInvoice: async (invoiceData) => {
    set({
      loading: true,
      error: null,
    });

    try {
      const token = useAuthStore.getState().accessToken;

      const response = await createInvoiceService(invoiceData, token);

      const invoice = response.invoice || response;

      set({
        invoice,
        loading: false,
      });

      return invoice;
    } catch (error) {
      set({
        error: error.response?.data?.error || 'No se pudo completar la compra.',
        loading: false,
      });

      throw error;
    }
  },

  clearInvoice: () => {
    set({
      invoice: null,
      error: null,
    });
  },
}));
