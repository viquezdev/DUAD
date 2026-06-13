async function getUser(userId) {
  try {
    const response = await fetch(`https://dummyjson.com/users/${userId}`);
    if (!response.ok) {
      throw new Error("User not found");
    }
    const data = await response.json();
    console.log("Datos del usuario: ", data);
  } catch (error) {
    console.log(`3. Hubo un problema: ${error}`);
    throw error;
  }
}

async function run() {
  try {
    await getUser(2);
    await getUser(3);
    await getUser(4);
  } catch (error) {
    console.log("Hubo un error");
  }
}

run();
