async function getUser(userId) {
  console.log("1. Enviando request");

  try {
    const response = await fetch(`https://dummyjson.com/users/${userId}`);

    console.log("2. Response recibido");

    if (!response.ok) {
      throw new Error("Error en la respuesta");
    }

    const data = await response.json();

    console.log("Datos del usuario:", data);

  } catch (error) {
    console.log(`3. Hubo un problema: ${error}`);
  }
}

const id = 2;
getUser(id);

console.log("5. Codigo llegado al final");


