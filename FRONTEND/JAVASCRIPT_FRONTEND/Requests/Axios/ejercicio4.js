const axios = require("axios");

async function updateUserAddress(id, address) {
  try {
    const url = "https://httpbin.org/put";

    const userData = {
      id: id,
      address: address,
    };

    const response = await axios.put(url, userData);
    console.log(response.status);
    return response.data;
  } catch (error) {
    console.log("error updating address");
    throw error;
  }
}

async function updateUserAndLogData() {
  try {
    const userData = await updateUserAddress(2, "san joaquin de flores");
    console.log(userData);
  } catch (error) {
    console.log(error);
  }
}

updateUserAndLogData();
