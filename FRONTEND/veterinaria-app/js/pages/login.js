import { saveSession } from "../services/sessionService.js";

const form = document.querySelector(".login-form");
const message = document.querySelector(".error-message");

form.addEventListener("submit", function (event) {
  event.preventDefault();

  const username = document.querySelector("#username").value;
  const password = document.querySelector("#password").value;

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
    console.log(data);

  } catch (error) {
    console.log(error);

    if (error.response) {
      message.textContent = error.response.data.message;
    } else {
      message.textContent = "Error al conectar con el servidor";
    }
  }
}

