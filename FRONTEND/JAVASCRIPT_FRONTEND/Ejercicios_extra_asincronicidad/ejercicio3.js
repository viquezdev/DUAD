function wait(seconds) {
  return new Promise((resolve) => {
    setTimeout(() => {
      console.log("Han pasado ", seconds, " segundos");
      resolve();
    },seconds );
  });
}


wait(2000)
  .then(() => wait(3000))
  .then(() => wait(1000));

