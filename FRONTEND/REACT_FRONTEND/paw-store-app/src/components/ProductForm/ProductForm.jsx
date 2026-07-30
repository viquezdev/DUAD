import { Formik, Form, Field } from 'formik';
import * as Yup from 'yup';
import './ProductForm.css';
import { useProductStore } from '../../store/productStore';
import { useState } from 'react';

const esquemaValidacion = Yup.object({
  sku: Yup.string().required('El SKU es obligatorio'),
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
  quantity: Yup.number()
    .typeError('Debe ingresar un número válido')
    .min(0, 'La cantidad no puede ser negativa')
    .required('La cantidad es obligatoria'),
});

export const ProductForm = ({ mode = 'create', product = null, setPage }) => {
  const createProduct = useProductStore((state) => state.createProduct);
  const updateProduct = useProductStore((state) => state.updateProduct);

  const [errorMessage, setErrorMessage] = useState('');
  return (
    <div className="formContainer">
      <h1>
        {mode === 'create' ? 'Agregar nuevo producto' : 'Editar producto'}
      </h1>

      <Formik
        initialValues={{
          sku: product?.sku || '',
          nombre: product?.name || '',
          descripcion: product?.description || '',
          precio: product?.price || 0,
          categoria: product?.category || '',
          imagen: product?.image || '',
          quantity: product?.quantity || 0,
        }}
        validationSchema={esquemaValidacion}
        onSubmit={async (values, { resetForm }) => {
          if (mode === 'create') {
            const apiNewProduct = {
              sku: values.sku,
              name: values.nombre,
              description: values.descripcion,
              price: values.precio,
              quantity: values.quantity,
              category: values.categoria,
              image: values.imagen,
            };
            try {
              await createProduct(apiNewProduct);
              resetForm();
              setErrorMessage('');
            } catch (error) {
              setErrorMessage(
                error.response?.data?.error || 'No se pudo agregar el producto.'
              );
            }
          } else {
            const apiUpdateProduct = {
              id: product.id,
              name: values.nombre,
              description: values.descripcion,
              price: values.precio,
              quantity: values.quantity,
              category: values.categoria,
              image: values.imagen,
            };
            try {
              await updateProduct(apiUpdateProduct);
              setPage('adminProducts');
            } catch (error) {
              setErrorMessage(
                error.response?.data?.error ||
                  'No se pudo actualizar el producto.'
              );
            }
          }
        }}
      >
        {({ isValid, submitCount }) => (
          <Form>
            <label htmlFor="sku">
              SKU <span aria-hidden="true">*</span>
            </label>

            <Field
              id="sku"
              name="sku"
              type="text"
              placeholder="Ej. PROD-001"
              aria-required="true"
            />

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

            <label htmlFor="quantity">
              Cantidad <span aria-hidden="true">*</span>
            </label>

            <Field
              id="quantity"
              name="quantity"
              type="number"
              min="0"
              aria-required="true"
              aria-describedby="quantity-error"
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
