//Revertir un string sin usar .reverse()

const word = "JavaScript";
function wordReverse(word) {
  let newWord = "";
  for (let number = word.length - 1; number >= 0; number--) {
    newWord += word[number];
  }
  return newWord;
}

console.log(wordReverse(word));

//Eliminar números duplicados de una lista
const list = [1, 2, 3, 2, 4, 1, 5];
function removeDuplicatedItems(list) {
  const unique = [...new Set(list)];
  return unique;
}
console.log(removeDuplicatedItems(list));

//Contador de palabras en un texto
const phrase = "This is a test. This test is simple.";
function wordCounter(phrase) {
  let counter = {};
  phraseArray = phrase.split(" ");
  phraseArray.forEach((word) => {
    counter[word] = (counter[word] || 0) + 1;
  });
  return counter;
}

console.log(wordCounter(phrase));
