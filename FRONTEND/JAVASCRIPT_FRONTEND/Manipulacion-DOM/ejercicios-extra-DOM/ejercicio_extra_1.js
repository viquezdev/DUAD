const button = document.getElementById("change-btn");

const changeColor = () => {
  let colors = ["red", "blue", "green", "orange", "purple"];
  let randomIndex = Math.floor(Math.random() * colors.length);
  let paragrahph = document.getElementById("text-info");
  paragrahph.style.color = colors[randomIndex];
};

button.addEventListener("click", changeColor);
