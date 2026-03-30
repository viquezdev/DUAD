const form = document.querySelector(".change-password-form");
const message = document.querySelector(".message");

form.addEventListener("submit", function (event) {
  event.preventDefault();

  const userId = document.querySelector("#user_id").value;
  const oldPassword = document.querySelector("#old_password").value;
  const newPassword = document.querySelector("#new_password").value;
  const confirmPassword = document.querySelector("#confirm_password").value;

  const registeredUser = JSON.parse(localStorage.getItem("registeredUser"));

  if (!registeredUser) {
    message.textContent = "El usuario no existe";
    return;
  }

  if (Number(userId) !== registeredUser.id) {
    message.textContent = "ID de usuario incorrecto";
    return;
  }

  if (oldPassword !== registeredUser.password) {
    message.textContent = "La contraseña anterior es incorrecta";
    return;
  }

  if (newPassword !== confirmPassword) {
    message.textContent = "Las contraseñas no coinciden";
    return;
  }

  registeredUser.password = newPassword;

  localStorage.setItem("registeredUser", JSON.stringify(registeredUser));

  message.textContent = "Contraseña actualizada correctamente";
  alert("contraseña actualizada exitosamente");
  window.location.href = "login.html";
});
