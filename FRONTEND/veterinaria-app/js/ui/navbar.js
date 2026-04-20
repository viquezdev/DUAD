import { getSession, clearSession } from "../services/sessionService.js";

export function setupNavbar() {
  const loginBtn = document.querySelector("#btnLogin");
  const logoutBtn = document.querySelector("#btnLogout");
  const session = getSession();

  if (loginBtn) {
    loginBtn.addEventListener("click", () => {
      window.location.href = "login.html";
    });
  }

  if (logoutBtn) {
    logoutBtn.addEventListener("click", () => {
      const salir = confirm(
        "¿Deseas cerrar sesión? Tendrás que iniciar sesión nuevamente.",
      );
      if (salir) {
        clearSession();
        window.location.href = "login.html";
      }
    });
  }
}

export function renderNavbar() {
  const session = getSession();
  const loginBtn = document.querySelector("#btnLogin");
  const userInfo = document.querySelector("#userInfo");
  const logoutBtn = document.querySelector("#btnLogout");

  if (session) {
    loginBtn.classList.add("hidden");
    userInfo.textContent = "Usuario: " + session.user.username;
    userInfo.classList.remove("hidden");
    logoutBtn.classList.remove("hidden");
  } else {
    loginBtn.classList.remove("hidden");
    userInfo.classList.add("hidden");
    logoutBtn.classList.add("hidden");
  }
}
