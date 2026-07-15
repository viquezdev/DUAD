import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import './ProductForm.css';
import { useProductStore } from '../../store/productStore';
import { useState } from 'react';

const esquemaValidacion = Yup.object({
  nombre: Yup.string().required('El nombre del producto es obligatorio'),
  descripcion: Yup.string().required(
    'La descripción del producto es obligatoria'
  ),
  precio: Yup.number()
    .typeError('Debe ingresar un número válido')
    .positive('El precio debe ser mayor que cero')
    .required('El precio es obligatorio'),
  categoria: Yup.string().required('La categoría del producto es obligatoria'),
  imagen: Yup.string().required('La imagen del producto es obligatoria'),
  stock: Yup.number()
    .typeError('Debe ingresar un número válido')
    .min(0, 'El stock no puede ser negativo')
    .required('El stock es obligatorio'),
});

export const ProductForm = ({ mode = 'create', product = null, setPage }) => {
  const addProduct = useProductStore((state) => state.addProduct);
  const updateProduct = useProductStore((state) => state.updateProduct);
  const [message, setMessage] = useState('');
  return (
    <div className="formContainer">
      <h1>
        {mode === 'create' ? 'Agregar nuevo producto' : 'Editar producto'}
      </h1>

      {message && <div className="successMessage">{message}</div>}

      <Formik
        initialValues={{
          nombre: product?.nombre || '',
          descripcion: product?.descripcion || '',
          precio: product?.precio || 0,
          categoria: product?.categoria || '',
          imagen: product?.imagen || '',
          stock: product?.stock || 0,
        }}
        validationSchema={esquemaValidacion}
        onSubmit={(values, { resetForm }) => {
          if (mode === 'create') {
            addProduct(values);
            resetForm();

            setMessage('Producto agregado correctamente');
          } else {
            updateProduct({
              ...product,
              ...values,
            });

            setMessage('Producto actualizado correctamente');
          }
        }}
      >
        <Form>
          <label htmlFor="nombre">
            Nombre <span aria-hidden="true">*</span>
          </label>

          <Field
            id="nombre"
            name="nombre"
            type="text"
            placeholder="Nombre del producto"
            aria-required="true"
            aria-describedby="nombre-help nombre-error"
          />

          <small id="nombre-help">Escriba el nombre del producto.</small>

          <ErrorMessage
            name="nombre"
            render={(msg) => (
              <p id="nombre-error" className="error" role="alert">
                {msg}
              </p>
            )}
          />

          <label htmlFor="descripcion">
            Descripción <span aria-hidden="true">*</span>
          </label>

          <Field
            id="descripcion"
            name="descripcion"
            as="textarea"
            rows="5"
            placeholder="Descripción detallada del producto"
            aria-required="true"
            aria-describedby="descripcion-error"
          />

          <ErrorMessage
            name="descripcion"
            render={(msg) => (
              <p id="descripcion-error" className="error" role="alert">
                {msg}
              </p>
            )}
          />

          <label htmlFor="precio">
            Precio <span aria-hidden="true">*</span>
          </label>

          <Field
            id="precio"
            name="precio"
            type="number"
            min="0"
            aria-required="true"
            aria-describedby="precio-help precio-error"
          />

          <small id="precio-help">Ingrese el precio en colones.</small>

          <ErrorMessage
            name="precio"
            render={(msg) => (
              <p id="precio-error" className="error" role="alert">
                {msg}
              </p>
            )}
          />

          <label htmlFor="categoria">
            Categoría <span aria-hidden="true">*</span>
          </label>

          <Field
            id="categoria"
            name="categoria"
            placeholder="Ej. Alimento, Juguetes..."
            aria-required="true"
            aria-describedby="categoria-error"
          />

          <ErrorMessage
            name="categoria"
            render={(msg) => (
              <p id="categoria-error" className="error" role="alert">
                {msg}
              </p>
            )}
          />

          <label htmlFor="imagen">
            Imagen <span aria-hidden="true">*</span>
          </label>

          <Field
            id="imagen"
            name="imagen"
            placeholder="https://..."
            aria-required="true"
            aria-describedby="imagen-error"
          />

          <ErrorMessage
            name="imagen"
            render={(msg) => (
              <p id="imagen-error" className="error" role="alert">
                {msg}
              </p>
            )}
          />

          <label htmlFor="stock">
            Stock <span aria-hidden="true">*</span>
          </label>

          <Field
            id="stock"
            name="stock"
            type="number"
            min="0"
            aria-required="true"
            aria-describedby="stock-error"
          />
          <ErrorMessage
            name="stock"
            render={(msg) => (
              <p id="stock-error" className="error" role="alert">
                {msg}
              </p>
            )}
          />

          <div className="formButtons">
            <button type="submit" className="btnSubmit">
              {mode === 'create' ? 'Agregar producto' : 'Guardar cambios'}
            </button>

            <button
              type="button"
              className="btnCancel"
              onClick={() => setPage('products')}
            >
              Cancelar
            </button>
          </div>
        </Form>
      </Formik>
    </div>
  );
};
