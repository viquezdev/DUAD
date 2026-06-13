






const button = document.getElementById("random-btn");

function changeColor(showCallBack)
{
  const arrayColors=['#FF5733', '#33FF57', '#3357FF', '#F5FF33', '#FF33F6'];
  let randomIndex = Math.floor(Math.random() * arrayColors.length);
  let square = document.getElementById("square");
  square.style.backgroundColor = arrayColors[randomIndex];
  showCallBack(arrayColors[randomIndex]);
};

function showCallBack(nameColor){
    const paragraph=document.getElementById("color-name");
    paragraph.textContent=nameColor;

}

button.addEventListener("click", () => {
  changeColor(showCallBack);
});