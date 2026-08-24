import './Checkout.css';
import { Formik, Form, Field } from 'formik';
import * as Yup from 'yup';
import { useCartStore } from '../store/cartStore';
import { useProductStore } from '../store/productStore';
import { useNavigate } from 'react-router-dom';
import { useInvoiceStore } from '../store/invoiceStore';
import { useAuthStore } from '../store/authStore';

const esquemaValidacion = Yup.object({
  nombre: Yup.string().required('El nombre completo es obligatorio'),
  email: Yup.string().email().required('El correo electrónico es obligatorio'),
  direccion: Yup.string().required('La dirección es obligatoria'),
  telefono: Yup.string().required('La número de teléfono es obligatorio'),
});

export const Checkout = () => {
  const cartItems = useCartStore((state) => state.cartItems);
  const products = useProductStore((state) => state.products);
  const navigate = useNavigate();
  const cart = useCartStore((state) => state.cart);
  const createInvoice = useInvoiceStore((state) => state.createInvoice);
  const user = useAuthStore((state) => state.user);
  return (
    <div className="checkout-page">
      <div className="purchase-information">
        <h1>Información de compra</h1>
        <Formik
          initialValues={{
            nombre: '',
            email: '',
            direccion: '',
            telefono: '',
          }}
          validationSchema={esquemaValidacion}
          onSubmit={async (values) => {
            try {
              const invoiceData = {
                user_id: user.id,
                shopping_cart_id: cart.id,
                billing_address: values.direccion,
                payment_method: 'credit_card',
                payment_status: 'pending',
                full_name: values.nombre,
                phone_number: values.telefono,
                email: values.email,
              };

              const invoice = await createInvoice(invoiceData);

              console.log('Factura creada:', invoice);

              // me falta poner enlace para la  página de confirmación
            } catch (error) {
              console.error('Error al completar la compra:', error);
            }
          }}
        >
          {({ isValid, submitCount }) => (
            <Form id="checkout-form">
              <label htmlFor="nombre">
                Nombre completo <span aria-hidden="true">*</span>
              </label>

              <Field
                id="nombre"
                name="nombre"
                type="text"
                placeholder="Nombre completo"
                aria-required="true"
                aria-describedby="nombre-help nombre-error"
              />

              <small id="nombre-help">Escriba el nombre completo.</small>

              <label htmlFor="email">
                Correo electrónico <span aria-hidden="true">*</span>
              </label>

              <Field
                id="email"
                name="email"
                type="email"
                placeholder="nombre.apellido@ejemplo.com"
                aria-required="true"
                aria-describedby="email-error"
              />

              <label htmlFor="direccion">
                Dirección <span aria-hidden="true">*</span>
              </label>

              <Field
                id="direccion"
                name="direccion"
                type="text"
                placeholder="Dirección"
                aria-required="true"
                aria-describedby="direccion-error"
              />

              <label htmlFor="telefono">
                Teléfono <span aria-hidden="true">*</span>
              </label>

              <Field
                id="telefono"
                name="telefono"
                placeholder="teléfono"
                aria-required="true"
                aria-describedby="telefono-error"
              />

              <p>Esta información se utilizará para completar la compra.</p>

              {!isValid && submitCount > 0 && (
                <p className="formError" role="alert">
                  Por favor completa todos los campos para completar la compra.
                </p>
              )}
            </Form>
          )}
        </Formik>
      </div>
      <div className="order-summary">
        <h1>Resumen del pedido</h1>
        <ul>
          {cartItems.map((item) => {
            const product = products.find(
              (product) => product.id === item.product_id
            );

            if (!product) {
              return null;
            }

            return (
              <li key={item.product_id}>
                <div className="items-summary">
                  <h2>{product.name}</h2>
                  <p>
                    {product.quantity} x ₡ {product.price}{' '}
                  </p>
                  <div className="item-price">
                    <p>Subtotal ₡{product.price}</p>
                  </div>
                </div>
              </li>
            );
          })}
        </ul>
        <p className="total">
          Total: ₡{' '}
          {cartItems
            .reduce((total, item) => total + Number(item.subtotal), 0)
            .toFixed(2)}{' '}
        </p>
        <button type="submit" form="checkout-form" className="btn-confirm">
          Confirmar compra
        </button>
        <button className="btn-cancel" onClick={() => navigate('/cart')}>
          Cancelar
        </button>
      </div>
    </div>
  );
};
