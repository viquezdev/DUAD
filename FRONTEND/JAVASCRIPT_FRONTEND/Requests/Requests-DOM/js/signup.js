const form = document.querySelector(".register-form");

form.addEventListener("submit", async function (event) {
  event.preventDefault();
  const userId = Date.now();
  const name = document.querySelector("#full_name").value;
  const email = document.querySelector("#email").value;
  const password = document.querySelector("#password").value;
  const address = document.querySelector("#address").value;

  try {
    const userData = await createUser(name, email, password, address);

    alert("Usuario creado correctamente! Tu id es " + userData.id);

    localStorage.setItem(
      "user",
      JSON.stringify({ id: userId, ...userData.json }),
    );

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
    console.log(response.status);
    const data = await response.data;
    return data;
  } catch (error) {
    console.log("error creating user");
    throw error;
  }
}
