const button = document.getElementById("change-btn");

const changeColor = () => {
  let colors = ["red", "blue", "green", "yellow", "cyan", "pink"];
  let randomIndex = Math.floor(Math.random() * colors.length);
  let paragraph = document.getElementById("text-info");
  paragraph.style.backgroundColor = colors[randomIndex];
};

button.addEventListener("click", changeColor);
