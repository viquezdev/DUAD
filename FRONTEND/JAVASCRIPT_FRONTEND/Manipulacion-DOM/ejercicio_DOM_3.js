window.onload = function () {
  document.getElementById("campo-empleo").style.display = "none";
};
const empleadoSi = document.getElementById("empleado_si");
const empleadoNo = document.getElementById("empleado_no");

const showInfo = () => {
  const empleadoSi = document.getElementById("empleado_si");
  const empresaInfo = document.getElementById("campo-empleo");
  if (empleadoSi.checked) {
    empresaInfo.style.display = "block";
  } else {
    empresaInfo.style.display = "none";
  }
};

empleadoSi.addEventListener("change", showInfo);
empleadoNo.addEventListener("change", showInfo);
