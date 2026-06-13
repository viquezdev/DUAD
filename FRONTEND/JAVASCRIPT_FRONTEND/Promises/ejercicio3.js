function wordPromise(word, time) {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve(word);
    }, time);
  });
}

const p1 = wordPromise("very", 1000);
const p2 = wordPromise("dogs", 500);
const p3 = wordPromise("cute", 1500);
const p4 = wordPromise("are", 800);

Promise.all([p1, p2, p3, p4])
  .then(words => {
    console.log(
      words[1],
      words[3], 
      words[0], 
      words[2] 
    );
  });