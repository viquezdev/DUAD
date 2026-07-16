import { Formik, Form, Field } from 'formik';
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
  const products = useProductStore((state) => state.products);
  const setSuccessMessage = useProductStore((state) => state.setSuccessMessage);
  const [errorMessage, setErrorMessage] = useState('');
  return (
    <div className="formContainer">
      <h1>
        {mode === 'create' ? 'Agregar nuevo producto' : 'Editar producto'}
      </h1>

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

            setSuccessMessage('Producto agregado correctamente');
          } else {
            const updated = products.some((p) => p.id === product?.id);

            if (!updated) {
              setErrorMessage('No se encontró el producto para actualizar.');
              return;
            }
            updateProduct({
              ...product,
              ...values,
            });

            setSuccessMessage('Producto actualizado correctamente');

            setPage('adminProducts');
          }
        }}
      >
        {({ isValid, submitCount }) => (
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

            <div className="formButtons">
              <button type="submit" className="btnSubmit">
                {mode === 'create' ? 'Agregar producto' : 'Guardar cambios'}
              </button>

              <button
                type="button"
                className="btnCancel"
                onClick={() =>
                  setPage(mode === 'edit' ? 'adminProducts' : 'products')
                }
              >
                Cancelar
              </button>
            </div>
            {errorMessage && (
              <p className="formError" role="alert">
                {errorMessage}
              </p>
            )}

            {!isValid && submitCount > 0 && (
              <p className="formError" role="alert">
                {mode === 'create'
                  ? 'Por favor completa todos los campos antes de agregar el producto.'
                  : 'Por favor completa todos los campos antes de guardar los cambios.'}
              </p>
            )}
          </Form>
        )}
      </Formik>
    </div>
  );
};
