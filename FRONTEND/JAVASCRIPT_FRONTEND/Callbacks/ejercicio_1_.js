function functionA(someParameter, functionB, functionC) {
  if(someParameter%2===0){
        functionB();
  }
  else{
     functionC();
  }
  
  
}

function functionB(){
   console.log("The number is even!"); 
}
function functionC(){
   console.log("The number is odd!"); 
}


functionA(3, functionB,functionC);