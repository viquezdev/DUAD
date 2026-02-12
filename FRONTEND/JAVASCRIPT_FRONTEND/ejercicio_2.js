//Toma un string y conviertelo en una lista de palabras, separandolas por espacios en blanco. No puedes usar la función split.
const example = "This is a string!"
let result=[];
let word="";
for(const letter  of example ){
    while(letter!=" "){
        word.concat(letter);
    }
    result.push(word)
    word=""
}
    
console.log(result)