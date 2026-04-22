import { setupNavbar } from "../ui/navbar.js";

setupNavbar();

const form = document.querySelector(".login-form");
const message = document.querySelector(".error-message");

form.addEventListener("submit", function (event) {
  event.preventDefault();

  const username = document.querySelector("#username").value.trim();
  const email = document.querySelector("#email").value.trim();
  const password = document.querySelector("#password").value;
  const verifyPassword = document.querySelector("#verify-password").value;

  if (password !== verifyPassword) {
    message.textContent = "Verifica que ambas contraseñas sean iguales";
    return;
  }

  message.textContent = "";

  registerUser(username, email, password);
});

async function registerUser(username, email, password) {
  try {
    const ahora = new Date();
    const timestamp = ahora.toISOString().slice(0, -1);
    const url = "http://localhost:5000/users/users";

    const userData = {
      username: username,
      email: email,
      password: password,
      is_admin: false,
      created_at: timestamp,
      updated_at: timestamp,
    };

    const response = await axios.post(url, userData);

    const data = response.data;

    alert("Registro exitoso, ya puedes iniciar sesión.");
    window.location.href = "login.html";
    console.log(data);
  } catch (error) {
    console.log(error);

    if (error.response) {
      message.textContent = error.response.data.error;
    } else {
      message.textContent = "Error al conectar con el servidor";
    }
  }
}
