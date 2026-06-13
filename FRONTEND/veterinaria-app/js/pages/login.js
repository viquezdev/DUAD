import { saveSession } from "../services/sessionService.js";

const form = document.querySelector(".login-form");
const message = document.querySelector(".error-message");

function validate(username, password) {
  if (!username.trim()) return "El usuario no puede estar vacío.";
  if (!password.trim()) return "La contraseña no puede estar vacía.";
  return null;
}

form.addEventListener("submit", function (event) {
  event.preventDefault();

  const username = document.querySelector("#username").value;
  const password = document.querySelector("#password").value;

  message.textContent = "";

  const error = validate(username, password);
  if (error) {
    message.textContent = error;
    return;
  }

  loginUser(username, password);
});

async function loginUser(username, password) {
  try {
    const url = "http://localhost:5000/users/login";

    const userData = {
      username: username,
      password: password,
    };

    const response = await axios.post(url, userData);

    const data = response.data;
    saveSession(data);
    alert("Login exitoso");
    window.location.href = "index.html";
  } catch (error) {
    console.log(error);

    if (error.response) {
      message.textContent = error.response.data.error;
    } else {
      message.textContent = "Error al conectar con el servidor";
    }
  }
}
