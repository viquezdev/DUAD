import { create } from 'zustand';
import { createInvoiceService } from '../services/invoiceService';

export const useInvoiceStore = create((set) => ({
  invoice: null,
  purchaseItems: [],
  loading: false,
  error: null,

  createInvoice: async (invoiceData, token) => {
    set({
      loading: true,
      error: null,
    });

    try {
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

  setPurchaseItems: (items) => {
    set({
      purchaseItems: items,
    });
  },

  clearInvoice: () => {
    set({
      invoice: null,
      purchaseItems: [],
      error: null,
    });
  },
}));
