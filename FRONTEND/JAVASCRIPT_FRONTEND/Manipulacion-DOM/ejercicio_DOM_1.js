const buttonAdd = document.getElementById("add-button");
const buttonClear = document.getElementById("clear-button");

const addItem = () => {
  const item = document.createElement("li");
  item.innerHTML = "Another item";
  const list = document.getElementById("list");
  list.appendChild(item);
};

const clearList = () => {
  const list = document.getElementById("list");
  list.innerHTML = "";
};

buttonAdd.addEventListener("click", addItem);
buttonClear.addEventListener("click", clearList);
