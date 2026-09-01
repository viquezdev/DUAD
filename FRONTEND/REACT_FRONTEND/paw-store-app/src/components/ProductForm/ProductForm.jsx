import { Formik, Form, Field } from 'formik';
import * as Yup from 'yup';
import './ProductForm.css';
import { useProductStore } from '../../store/productStore';
import { useNavigate } from 'react-router-dom';
import { useState } from 'react';

const validationSchema = Yup.object({
  sku: Yup.string().required('El SKU es obligatorio'),
  name: Yup.string().required('El nombre del producto es obligatorio'),
  description: Yup.string().required(
    'La descripción del producto es obligatoria'
  ),
  price: Yup.number()
    .typeError('Debe ingresar un número válido')
    .positive('El precio debe ser mayor que cero')
    .required('El precio es obligatorio'),
  category: Yup.string().required('La categoría del producto es obligatoria'),
  image: Yup.string().required('La imagen del producto es obligatoria'),
  quantity: Yup.number()
    .typeError('Debe ingresar un número válido')
    .min(0, 'La cantidad no puede ser negativa')
    .required('La cantidad es obligatoria'),
});

export const ProductForm = ({ mode = 'create', product = null }) => {
  const createProduct = useProductStore((state) => state.createProduct);
  const updateProduct = useProductStore((state) => state.updateProduct);
  const navigate = useNavigate();
  const [errorMessage, setErrorMessage] = useState('');

  return (
    <div className="formContainer">
      <h1>
        {mode === 'create' ? 'Agregar nuevo producto' : 'Editar producto'}
      </h1>

      <Formik
        initialValues={{
          sku: product?.sku || '',
          name: product?.name || '',
          description: product?.description || '',
          price: product?.price || 0,
          category: product?.category || '',
          image: product?.image || '',
          quantity: product?.quantity || 0,
        }}
        validationSchema={validationSchema}
        onSubmit={async (values, { resetForm }) => {
          if (mode === 'create') {
            const newProduct = {
              sku: values.sku,
              name: values.name,
              description: values.description,
              price: values.price,
              quantity: values.quantity,
              category: values.category,
              image: values.image,
            };

            try {
              await createProduct(newProduct);
              resetForm();
              setErrorMessage('');
            } catch (error) {
              setErrorMessage(
                error.response?.data?.error || 'No se pudo agregar el producto.'
              );
            }
          } else {
            const updatedProduct = {
              id: product.id,
              name: values.name,
              description: values.description,
              price: values.price,
              quantity: values.quantity,
              category: values.category,
              image: values.image,
            };

            try {
              await updateProduct(updatedProduct);
              navigate('/admin/products');
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
              readOnly={mode === 'edit'}
            />

            <label htmlFor="name">
              Nombre <span aria-hidden="true">*</span>
            </label>

            <Field
              id="name"
              name="name"
              type="text"
              placeholder="Nombre del producto"
              aria-required="true"
              aria-describedby="name-help name-error"
            />

            <small id="name-help">Escriba el nombre del producto.</small>

            <label htmlFor="description">
              Descripción <span aria-hidden="true">*</span>
            </label>

            <Field
              id="description"
              name="description"
              as="textarea"
              rows="5"
              placeholder="Descripción detallada del producto"
              aria-required="true"
              aria-describedby="description-error"
            />

            <label htmlFor="price">
              Precio <span aria-hidden="true">*</span>
            </label>

            <Field
              id="price"
              name="price"
              type="number"
              min="0"
              aria-required="true"
              aria-describedby="price-help price-error"
            />

            <small id="price-help">Ingrese el precio en colones.</small>

            <label htmlFor="category">
              Categoría <span aria-hidden="true">*</span>
            </label>

            <Field
              id="category"
              name="category"
              placeholder="Ej. Alimento, Juguetes..."
              aria-required="true"
              aria-describedby="category-error"
            />

            <label htmlFor="image">
              Imagen <span aria-hidden="true">*</span>
            </label>

            <Field
              id="image"
              name="image"
              placeholder="https://..."
              aria-required="true"
              aria-describedby="image-error"
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
                  navigate(mode === 'edit' ? '/admin/products' : '/products')
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
