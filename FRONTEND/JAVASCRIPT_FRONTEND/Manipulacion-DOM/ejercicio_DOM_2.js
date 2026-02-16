const button = document.getElementById("show-button");

const showInfo = () => {
  let input = document.getElementById("info");
  let text = document.getElementById("info").value;

  alert(text);
  input.value = "";
};

const clearList = () => {
  const list = document.getElementById("list");
  list.innerHTML = "";
};

button.addEventListener("click", showInfo);
