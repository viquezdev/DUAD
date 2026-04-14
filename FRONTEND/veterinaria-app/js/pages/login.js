const form = document.querySelector(".login-form");
const message = document.querySelector(".error-message");

form.addEventListener("submit", function (event) {
  event.preventDefault();

  const email = document.querySelector("#email").value;
  const password = document.querySelector("#password").value;

  const registeredUser = JSON.parse(localStorage.getItem("registeredUser"));

  if (!registeredUser) {
    message.textContent = "Usuario no existe";
    return;
  }

  if (
    Number(userId) === registeredUser.id &&
    password === registeredUser.password
  ) {
    localStorage.setItem("sessionUser", JSON.stringify(registeredUser));
    window.location.href = "profile.html";
  } else {
    message.textContent = "ID o contraseña incorrectos";
  }
});
