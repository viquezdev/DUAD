const axios = require("axios");

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

async function createUserAndLogData() {
  try {
    const userData = await createUser(
      "LUIS VIQUEZ",
      "luis@gmail.com",
      "123456",
      "san joaquin",
    );
    console.log(userData);
  } catch (error) {
    console.log(error);
  }
}

createUserAndLogData();
