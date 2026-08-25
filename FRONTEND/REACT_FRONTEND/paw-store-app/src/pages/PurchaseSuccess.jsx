import './PurchaseSuccess.css';
import { useNavigate } from 'react-router-dom';

import { useInvoiceStore } from '../store/invoiceStore';
import { useCartStore } from '../store/cartStore';
import { useProductStore } from '../store/productStore';

export const PurchaseSuccess = () => {
  const navigate = useNavigate();

  const invoice = useInvoiceStore((state) => state.invoice);

  const cartItems = useCartStore((state) => state.cartItems);

  const products = useProductStore((state) => state.products);

  const clearData = useCartStore((state) => state.clearCart);

  if (!invoice) {
    return (
      <div className="purchase-success-page">
        <section className="success-card">
          <h1>No hay información de compra</h1>

          <p>No se encontró información sobre la compra realizada.</p>

          <button className="btn-catalog" onClick={() => navigate('/products')}>
            Volver al catálogo
          </button>
        </section>
      </div>
    );
  }

  return (
    <div className="purchase-success-page">
      <section className="success-card">
        <div className="success-icon" aria-hidden="true">
          ✓
        </div>

        <h1>Compra realizada con éxito</h1>

        <p>
          Tu pedido ha sido procesado correctamente. Recibirás un correo con la
          confirmación y los detalles de tu compra.
        </p>

        <p className="invoice-number">
          Factura: <strong>{invoice.invoice_number}</strong>
        </p>
      </section>

      <section className="purchase-summary">
        <h2>Resumen de la compra</h2>

        <div className="summary-divider"></div>

        <div className="summary-header">
          <span>Producto</span>
          <span>Cantidad</span>
          <span>Precio Unitario</span>
          <span>Subtotal</span>
        </div>

        {cartItems.map((item) => {
          const product = products.find(
            (product) => product.id === item.product_id
          );

          if (!product) {
            return null;
          }

          return (
            <div className="summary-item" key={item.product_id}>
              <span>{product.name}</span>

              <span>{item.quantity}</span>

              <span>
                ₡{' '}
                {Number(product.price).toLocaleString('es-CR', {
                  minimumFractionDigits: 2,
                  maximumFractionDigits: 2,
                })}
              </span>

              <span>
                ₡{' '}
                {Number(item.subtotal).toLocaleString('es-CR', {
                  minimumFractionDigits: 2,
                  maximumFractionDigits: 2,
                })}
              </span>
            </div>
          );
        })}

        <div className="summary-total">
          <strong>Total</strong>

          <strong>
            ₡{' '}
            {Number(invoice.total_amount).toLocaleString('es-CR', {
              minimumFractionDigits: 2,
              maximumFractionDigits: 2,
            })}
          </strong>
        </div>
      </section>

      <div className="success-actions">
        <button
          className="btn-catalog"
          onClick={() => {
            (clearData(), navigate('/products'));
          }}
        >
          Volver al catálogo
        </button>

        <button className="btn-home" onClick={() => navigate('/')}>
          Ir al inicio
        </button>
      </div>
    </div>
  );
};
