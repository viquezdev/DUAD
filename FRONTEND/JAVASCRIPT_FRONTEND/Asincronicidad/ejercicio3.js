async function getUser(userId) {
  console.log("1. Enviando request");

  try {
    const response = await fetch(`https://dummyjson.com/users/${userId}`);

    console.log("2. Response recibido");

    if (!response.ok) {
      throw new Error("User not found");
    }

    const data = await response.json();

    return data;

  } catch (error) {
    console.log(`3. Hubo un problema: ${error}`);
    return null;
  }
}







const button = document.getElementById("show-button");

const showInfo = async () => {
  let input = document.getElementById("info");
  let text = document.getElementById("info").value;
  const user = await getUser(text);
   if (!user) {
    alert("User not found");
    return;
  }
  alert(user.firstName + "\n" + user.lastName+ "\n"+user.email);
  input.value = "";
};



button.addEventListener("click", showInfo);
