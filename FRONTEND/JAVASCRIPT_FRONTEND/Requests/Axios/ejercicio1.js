const axios = require("axios");

async function listObjects() {
  try {
    const response = await axios.get(`https://api.restful-api.dev/objects`);
    const objects = await response.data;

    const filtered = objects.filter((obj) => obj.data);
    filtered.forEach((obj) => {
      const details = Object.entries(obj.data)
        .map(([key, value]) => `${key}: ${value}`)
        .join(", ");
      console.log(`${obj.name} (${details})`);
    });
  } catch (error) {
    console.log("error obteniendo datos");
  }
}

listObjects();
