import number from 'number';
console.log("Hello world!");

//Realiza un programa que recorra una lista e imprima todos sus elementos

const myArray=[1,2,3,4,5,6];
for(const number of myArray){
    console.log(number);
}


//Realiza un programa que recorra una lista de números y almacene todos los pares en otra lista
//Para este ejercicio intenta hacer una solución con un for y otra utilizando la función filter

const myArray2=[1,2,3,4,5,6];
const myArray3=[];
for(const number of myArray){
    
    if(number%2===0){
        myArray3.push(number);
    }
    
}
console.log(myArray3);

//Filter

const myArray4=[1,2,3,4,5,6];
const filtered=myArray4.filter(element=>element%2===0);
console.log(filtered);


//Toma una lista de temperaturas en grados celsius y conviertala a farenheit utilizando la función map
const temperaturasCelsius = [22.5, 19.0, 25.0, 31.2, 28.7, 15.1, 10.0];
const temperaturasFarenheit= temperaturasCelsius.map((element)=>{
    return (((element*9)/5)+32)
});;

console.log(temperaturasFarenheit)

//Toma un string y conviertelo en una lista de palabras, separandolas por espacios en blanco. No puedes usar la función split.
const example = "This is a string!";
let result=[];
let word="";
for(const letter  of example ){
    if (letter !== " "){
        word+=letter;
    }
    else{
    result.push(word);
    word="";
    }
}
    
console.log(result);