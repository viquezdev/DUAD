import { Formik, Form, Field, ErrorMessage } from 'formik';
import './ProductForm.css';
import * as Yup from 'yup';

const esquemaValidacion = Yup.object({
  nombre: Yup.string().required('El nombre del producto es obligatorio'),
  descripcion: Yup.string().required(
    'La descripción del producto es obligatoria'
  ),
  precio: Yup.number().required('El precio es obligatorio'),
  categoria: Yup.string().required('La categoría del producto es obligatoria'),
  imagen: Yup.string().required('La imagen del producto es obligatoria'),
  stock: Yup.number().required('El stock del producto es obligatorio'),
});
export const ProductForm = () => {
  return (
    <div className="formContainer">
      <h1>Agregar nuevo producto</h1>
      <Formik
        initialValues={{
          nombre: '',
          descripcion: '',
          precio: 0,
          categoria: '',
          imagen: '',
          stock: 0,
        }}
        validationSchema={esquemaValidacion}
        onSubmit={(valores) => {
          alert(JSON.stringify(valores, null, 6));
        }}
      >
        <Form>
          <label htmlFor="nombre">Nombre</label>
          <Field id="nombre" name="nombre" placeholder="Nombre del producto" />
          <ErrorMessage name="nombre" component="p" />

          <label htmlFor="descripcion">Descripción</label>
          <Field
            id="descripcion"
            name="descripcion"
            as="textarea"
            rows="5"
            placeholder="Descripción detallada del producto"
          />
          <ErrorMessage name="descripcion" component="p" />

          <label htmlFor="precio">Precio</label>
          <Field id="precio" name="precio" type="number" />
          <ErrorMessage name="precio" component="p" />

          <label htmlFor="categoria">Categoría</label>
          <Field
            id="categoria"
            name="categoria"
            placeholder="Categoría del producto(ej. Alimento, Juguetes)"
          />
          <ErrorMessage name="categoria" component="p" />

          <label htmlFor="imagen">Imagen</label>
          <Field id="imagen" name="imagen" placeholder="Imagen del producto" />
          <ErrorMessage name="imagen" component="p" />

          <label htmlFor="stock">Stock</label>
          <Field id="stock" name="stock" type="number" />
          <ErrorMessage name="stock" component="p" />

          <button className="btnSubmit" type="submit">
            Agregar producto
          </button>
        </Form>
      </Formik>
    </div>
  );
};
