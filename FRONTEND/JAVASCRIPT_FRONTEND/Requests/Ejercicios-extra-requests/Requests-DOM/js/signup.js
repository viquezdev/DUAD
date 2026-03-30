const form = document.querySelector(".register-form");

form.addEventListener("submit", async function (event) {
  event.preventDefault();

  const userId = Date.now();

  const name = document.querySelector("#full_name").value;
  const email = document.querySelector("#email").value;
  const password = document.querySelector("#password").value;
  const address = document.querySelector("#address").value;

  try {
    await createUser(name, email, password, address);

    const user = {
      id: userId,
      name: name,
      email: email,
      password: password,
      address: address,
    };

    alert("Usuario creado correctamente! Tu id es " + userId);

    localStorage.setItem("registeredUser", JSON.stringify(user));

    const sessionData = {
      user: user,
      loginTime: Date.now()
    };

    localStorage.setItem("sessionUser", JSON.stringify(sessionData));

    window.location.href = "profile.html";
  } catch (error) {
    alert("Error creating user");
  }
});

async function createUser(name, email, password, address) {
  try {
    const url = "https://httpbin.org/post";

    const userData = {
      name: name,
      email: email,
      password: password,
      address: address,
    };

    const response = await axios.post(url, userData);

    return response.data;
  } catch (error) {
    console.log("error creating user");
    throw error;
  }
}
