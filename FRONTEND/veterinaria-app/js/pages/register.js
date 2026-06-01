import { setupNavbar } from "../ui/navbar.js";

setupNavbar();

const form = document.querySelector(".login-form");
const message = document.querySelector(".error-message");


const RULES = {
  username: {
    minLength: 3,
    maxLength: 20,
    pattern: /^[a-zA-Z0-9_]+$/ 
  },
  password: {
    minLength: 6
  },
  email: {
    pattern:/^[^\s@]+@[^\s@]+\.[^\s@]+$/
  }
};


function validate(username, email, password, verifyPassword) {
  if (!username.trim()) return "El usuario no puede estar vacío.";
  if (username.length < RULES.username.minLength) return `El usuario debe tener al menos ${RULES.username.minLength} caracteres.`;
  if (!RULES.username.pattern.test(username)) return "El usuario solo puede contener letras, números y guión bajo.";

  if (!email.trim()) return "El email no puede estar vacío.";
  if (!RULES.email.pattern.test(email.trim())) return "El email no tiene el formato correcto.";

  if (!password.trim()) return "La contraseña no puede estar vacía.";
  if (password.length < RULES.password.minLength) return `La contraseña debe tener al menos ${RULES.password.minLength} caracteres.`;

  if (password !== verifyPassword) return "Verifica que ambas contraseñas sean iguales.";

  return null;
}


form.addEventListener("submit", function (event) {
  event.preventDefault();

  const username       = document.querySelector("#username").value;
  const email          = document.querySelector("#email").value;
  const password       = document.querySelector("#password").value;
  const verifyPassword = document.querySelector("#verify-password").value;

  message.textContent = "";

  const error = validate(username, email, password, verifyPassword);
  if (error) {
    message.textContent = error;
    return;
  }

  registerUser(username, email, password);
});


async function registerUser(username, email, password) {
  try {
    const url = "http://localhost:5000/users/users";

    const userData = {
      username: username,
      email: email,
      password: password,
    };

    const response = await axios.post(url, userData);

    const data = response.data;

    alert("Registro exitoso");
    window.location.href = "login.html";
    console.log(data);
  } catch (error) {
    if (error.response) {
      message.textContent = error.response.data.error || "Error al registrar";
    } else {
      message.textContent = "Error al conectar con servidor";
    }
  }
}
