const axios = require("axios");

async function getObject(id) {
  try {
    const response = await axios.get(
      `https://api.restful-api.dev/objects/${id}`,
    );

    return response.data;
  } catch (error) {
    if (error.response && error.response.status === 404) {
      console.log("Objeto no encontrado");
    } else {
      console.log("Error obteniendo datos");
    }
  }
}

async function fetchObject(id) {
  try {
    const objectData = await getObject(id);
    console.log(objectData);
  } catch (error) {
    console.log(error);
  }
}

fetchObject(600);
