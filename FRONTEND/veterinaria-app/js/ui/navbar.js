import { getSession } from "../services/sessionService.js";


export function setupNavbar(){

const loginBtn = document.querySelector("#btnLogin");

  if(loginBtn){
    loginBtn.addEventListener("click", () => {
      window.location.href = "login.html";
    });
  }

}


export function renderNavbar(){
  const session = getSession();
  const loginBtn = document.querySelector("#btnLogin");
  const userInfo = document.querySelector("#userInfo");
  const logoutBtn = document.querySelector("#btnLogout");
  

  if(session){
   loginBtn.classList.add("hidden");
   userInfo.textContent ="Usuario: " + session.user.username;
   userInfo.classList.remove("hidden");
   logoutBtn.classList.remove("hidden");
}
else{
   loginBtn.classList.remove("hidden");
   userInfo.classList.add("hidden");
   logoutBtn.classList.add("hidden");
}

}