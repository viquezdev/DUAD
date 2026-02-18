const buttonMinus = document.getElementById("minus-btn");
const buttonPlus = document.getElementById("plus-btn");

const sumNumber = () => {
  let element = document.getElementById("counter");
  let sum = parseInt(element.textContent) + 1;
  element.textContent = sum;
};

const decrementNumber = () => {
  let element = document.getElementById("counter");
  let subtraction = 0;
  if (parseInt(element.textContent) > 0) {
    subtraction = parseInt(element.textContent) - 1;
  }

  element.textContent = subtraction;
};

buttonMinus.addEventListener("click", decrementNumber);
buttonPlus.addEventListener("click", sumNumber);
