export function setupNavbar(){

  const loginBtn = document.querySelector("#btnLogin");

  if(loginBtn){
    loginBtn.addEventListener("click", () => {
      window.location.href = "login.html";
    });
  }

}