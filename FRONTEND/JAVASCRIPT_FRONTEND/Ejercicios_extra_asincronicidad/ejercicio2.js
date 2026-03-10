function loadResources(name, time) {
  return new Promise((resolve) => {

    console.log("Cargando", name);

    setTimeout(() => {

      console.log(name, "cargado");

      resolve(name);

    }, time );

  });
}

const img1 = loadResources("imagen1", 2000);
const img2 = loadResources("imagen2", 1000);
const img3 = loadResources("imagen3", 1500);

Promise.all([ img1, img2, img3 ])
  .then(() => {
    console.log("Imagenes cargadas");
  });


loadResources("script1", 1000)
  .then(() => loadResources("script2", 1500))
  .then(() => loadResources("script3", 800))
  .then(() => {
    console.log("Scripts cargados");

  })
  .then(() => {
    console.log("Todo el sitio cargado");
  });

