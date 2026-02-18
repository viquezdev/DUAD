window.onload = function () {
  document.getElementById("tasks-container").style.display = "none";
};
const buttonAdd = document.getElementById("add-btn");

const addTask = () => {
  let inputText = document.getElementById("text-info");
  const item = document.createElement("li");
  item.innerHTML = inputText.value;
  const deleteButton = document.createElement("button");
  deleteButton.textContent = "Delete";
  deleteButton.addEventListener("click", () => {
    item.remove();
  });
  item.appendChild(deleteButton);
  const list = document.getElementById("list-tasks");
  list.appendChild(item);
  document.getElementById("tasks-container").style.display = "block";
};

buttonAdd.addEventListener("click", addTask);
