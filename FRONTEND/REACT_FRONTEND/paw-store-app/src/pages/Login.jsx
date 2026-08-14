import { Formik, Form, Field } from 'formik';
import * as Yup from 'yup';
import { login } from '../services/authService';
import './Login.css';
import { useState } from 'react';
import { useAuthStore } from '../store/authStore';
import { useNavigate } from 'react-router-dom';

const esquemaValidacion = Yup.object({
  email: Yup.string().email().required('El correo electrónico es obligatorio'),
  password: Yup.string().required('La contraseña es obligatoria'),
});

export const Login = () => {
  const loginStore = useAuthStore((state) => state.login);
  const [errorMessage, setErrorMessage] = useState('');
  const navigate = useNavigate();

  return (
    <main className="login-page">
      <div className="loginContainer">
        <h1>Iniciar sesión</h1>
        {errorMessage && <p className="formError">{errorMessage}</p>}
        <Formik
          initialValues={{
            email: '',
            password: '',
          }}
          validationSchema={esquemaValidacion}
          onSubmit={async (values) => {
            try {
              const data = await login(values.email, values.password);
              loginStore(data.user, data.access_token, data.refresh_token);
              navigate(data.user.is_admin ? '/admin/products' : '/products');
            } catch (error) {
              if (error.response?.status === 401) {
                setErrorMessage(
                  'Las credenciales proporcionadas no son válidas. Por favor verifica tu correo y contraseña.'
                );
              } else {
                setErrorMessage(
                  'Ocurrió un error al conectar con el servidor.'
                );
              }
            }
          }}
        >
          {({ isValid, submitCount }) => (
            <Form>
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

              <label htmlFor="password">
                Contraseña <span aria-hidden="true">*</span>
              </label>

              <Field
                id="password"
                name="password"
                type="password"
                placeholder="Introduce tu contraseña"
                aria-required="true"
                aria-describedby="password-error"
              />
              {!isValid && submitCount > 0 && (
                <p className="formError" role="alert">
                  Por favor completa todos los campos para iniciar sesión.
                </p>
              )}
              <div className="formButtons">
                <button type="submit" className="btnSubmit">
                  Ingresar
                </button>

                <button
                  type="button"
                  className="btnCancel"
                  onClick={() => navigate('/')}
                >
                  Volver a inicio
                </button>
              </div>
            </Form>
          )}
        </Formik>
      </div>
    </main>
  );
};
