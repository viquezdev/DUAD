import './Checkout.css';
import { Formik, Form, Field } from 'formik';
import * as Yup from 'yup';
import { useCartStore, selectCartTotal } from '../store/cartStore';
import { useProductStore } from '../store/productStore';
import { useNavigate } from 'react-router-dom';
import { useInvoiceStore } from '../store/invoiceStore';
import { useAuthStore } from '../store/authStore';
import { useState, useEffect } from 'react';

const validationSchema = Yup.object({
  fullName: Yup.string().required('El nombre completo es obligatorio'),
  email: Yup.string()
    .email('El correo electrónico no es válido')
    .required('El correo electrónico es obligatorio'),
  address: Yup.string().required('La dirección es obligatoria'),
  phone: Yup.string().required('El número de teléfono es obligatorio'),
});

export const Checkout = () => {
  const cartItems = useCartStore((state) => state.cartItems);
  const products = useProductStore((state) => state.products);
  const navigate = useNavigate();
  const cart = useCartStore((state) => state.cart);
  const createInvoice = useInvoiceStore((state) => state.createInvoice);
  const user = useAuthStore((state) => state.user);
  const disableCheckout = useCartStore((state) => state.disableCheckout);
  const [purchaseError, setPurchaseError] = useState(null);
  const total = useCartStore(selectCartTotal);

  useEffect(() => {
    if (!user) {
      navigate('/login');
      return;
    }

    if (!cart || cartItems.length === 0) {
      navigate('/cart');
    }
  }, [user, cart, cartItems.length, navigate]);

  return (
    <>
      <h1>Checkout</h1>

      <div className="checkout-page">
        <div className="purchase-information">
          <h2>Información de compra</h2>

          <Formik
            initialValues={{
              fullName: '',
              email: '',
              address: '',
              phone: '',
            }}
            validationSchema={validationSchema}
            onSubmit={async (values) => {
              setPurchaseError(null);

              if (!cart || cartItems.length === 0) {
                setPurchaseError(
                  'No puedes completar la compra porque tu carrito está vacío.'
                );
                return;
              }

              if (!user) {
                navigate('/login');
                return;
              }

              try {
                const invoiceData = {
                  user_id: user.id,
                  shopping_cart_id: cart.id,
                  billing_address: values.address,
                  payment_method: 'credit_card',
                  payment_status: 'pending',
                  full_name: values.fullName,
                  phone_number: values.phone,
                  email: values.email,
                };

                const invoice = await createInvoice(invoiceData);

                if (invoice) {
                  navigate('/purchase-success');
                }
              } catch (error) {
                console.error('Error al completar la compra:', error);

                const errorMessage =
                  error.response?.data?.error ||
                  'Ocurrió un problema al procesar tu compra. Por favor intenta de nuevo.';

                setPurchaseError(errorMessage);
              }
            }}
          >
            {({ isValid, submitCount }) => (
              <Form id="checkout-form">
                <label htmlFor="fullName">
                  Nombre completo <span aria-hidden="true">*</span>
                </label>

                <Field
                  id="fullName"
                  name="fullName"
                  type="text"
                  placeholder="Nombre completo"
                  aria-required="true"
                  aria-describedby="fullName-help fullName-error"
                />

                <small id="fullName-help">Escriba el nombre completo.</small>

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

                <label htmlFor="address">
                  Dirección de envío <span aria-hidden="true">*</span>
                </label>

                <Field
                  id="address"
                  name="address"
                  type="text"
                  placeholder="Dirección de envío"
                  aria-required="true"
                  aria-describedby="address-error"
                />

                <label htmlFor="phone">
                  Teléfono <span aria-hidden="true">*</span>
                </label>

                <Field
                  id="phone"
                  name="phone"
                  type="tel"
                  placeholder="Teléfono"
                  aria-required="true"
                  aria-describedby="phone-error"
                />

                <p>Esta información se utilizará para completar la compra.</p>

                {!isValid && submitCount > 0 && (
                  <p className="formError" role="alert">
                    Por favor completa todos los campos para completar la
                    compra.
                  </p>
                )}
              </Form>
            )}
          </Formik>
        </div>

        <div className="order-summary">
          <h2>Resumen del pedido</h2>

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
                      {item.quantity} x ₡ {product.price}
                    </p>

                    <div className="item-price">
                      <p>Subtotal ₡{item.subtotal}</p>
                    </div>
                  </div>
                </li>
              );
            })}
          </ul>

          <p className="total">Total: ₡ {total}</p>

          {purchaseError && (
            <p className="formError" role="alert">
              {purchaseError}
            </p>
          )}

          <button type="submit" form="checkout-form" className="btn-confirm">
            Confirmar compra
          </button>

          <button
            className="btn-cancel"
            onClick={() => {
              disableCheckout();
              navigate('/cart');
            }}
          >
            Cancelar
          </button>
        </div>
      </div>
    </>
  );
};
