function wait(seconds) {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve(console.log("Han pasado ", seconds, " segundos"));
    }, time);
  });
}

const t1 = wait(2000);
const t2 = wait(3000);
const t3 = wait(1000);

Promise.all([t1, t2, t3]).then((times) => {
  console.log(times[0], times[1], times[2]);
});
