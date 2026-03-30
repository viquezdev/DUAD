const session = localStorage.getItem("sessionUser");

if (!session) {
  window.location.href = "login.html";
}

const sessionData = JSON.parse(session);
const userData = sessionData.user;

const now = Date.now();
const loginTime = sessionData.loginTime;

const sessionLimit = 5 * 60 * 1000;

if (now - loginTime > sessionLimit) {
  localStorage.removeItem("sessionUser");
  window.location.href = "login.html?expired=true";
}


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


const editBtn = document.querySelector(".edit-btn");

editBtn.addEventListener("click", function () {

  const editContainer = document.querySelector("#edit-container");

  editContainer.innerHTML = `
    <div class="edit-form">
      <h3>Edit Profile</h3>

      <input type="text" id="edit-name" value="${userData.name}" placeholder="Name">

      <input type="text" id="edit-address" value="${userData.address}" placeholder="Address">

      <button id="save-profile">Save</button>

      <p id="message"></p>
    </div>
  `;

  const saveBtn = document.querySelector("#save-profile");

  saveBtn.addEventListener("click", updateProfile);

});


async function updateProfile() {

  const newName = document.querySelector("#edit-name").value;
  const newAddress = document.querySelector("#edit-address").value;

  const message = document.querySelector("#message");

  try {
console.log(userData);
console.log(userData.id);
    const response = await fetch(`https://httpbin.org/patch`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        name: newName,
        data: {
          address: newAddress
        }
      })
    });
   console.log(response);
    if (!response.ok) {
      throw new Error("Error updating profile");
    }

    document.querySelector("#user-name").textContent = newName;
    document.querySelector("#user-address").textContent = newAddress;

    
    userData.name = newName;
    userData.address = newAddress;

    localStorage.setItem("sessionUser", JSON.stringify(userData));
    localStorage.setItem("registeredUser", JSON.stringify(userData));

    message.textContent = "Profile updated successfully";

  } catch (error) {

    message.textContent = "Error updating profile";

  }

}