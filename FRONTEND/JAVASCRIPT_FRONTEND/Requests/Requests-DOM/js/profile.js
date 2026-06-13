const session = localStorage.getItem("sessionUser");

if (!session) {
  window.location.href = "login.html";
}

const userData = JSON.parse(session);

document.querySelector("#user-name").textContent = userData.name;
document.querySelector("#user-email").textContent = userData.email;
document.querySelector("#user-address").textContent = userData.address;
document.querySelector("#user-id").textContent = userData.id;

const logoutBtn = document.querySelector(".logout-btn");

logoutBtn.addEventListener("click", function () {
  localStorage.removeItem("sessionUser");
  window.location.href = "login.html";
});

const passwordBtn = document.querySelector(".password-btn");

passwordBtn.addEventListener("click", function () {
  window.location.href = "change-password.html";
});
