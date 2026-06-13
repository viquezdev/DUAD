

const arrayNamesA=["Luis Viquez","Andrey Viquez","Jonathan Viquez"];
const arrayNamesB=["Pepe Ramirez","Luis Viquez","Elsy Garro"];

function  findCommonElements(arrayNamesA,arrayNamesB,printCallback){
    let arrayCommonElements=[];
    for(let i=0;i<arrayNamesA.length;i++){
        for(let j=0;j<arrayNamesB.length;j++){
            if(arrayNamesA[i]===arrayNamesB[j]){
                arrayCommonElements.push(arrayNamesA[i]);
            }
        }
    }
    printCallback(arrayCommonElements);


}







function printCallback(array){
    console.log("Found common elements: ",array);
}



findCommonElements(arrayNamesA,arrayNamesB,printCallback);

