import 'Checkout.css';
import { Formik, Form, Field } from 'formik';
import * as Yup from 'yup';

const esquemaValidacion = Yup.object({
  nombre: Yup.string().required('El nombre completo es obligatorio'),
  email: Yup.string().email().required('El correo electrónico es obligatorio'),
  direccion: Yup.string().required('La dirección es obligatoria'),
  telefono: Yup.string().required('La número de teléfono es obligatorio'),
});

export const Checkout = () => {
  return (
    <div className="checkout-page">
      <div className="purchase-information">
        <Formik
          initialValues={{
            nombre: '',
            email: '',
            direccion: '',
            telefono: '',
          }}
          validationSchema={esquemaValidacion}
          onSubmit={async () => {
            //logica para crear factura
          }}
        >
          {({ isValid, submitCount }) => (
            <Form>
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
      <div className="order-summary"></div>
    </div>
  );
};
