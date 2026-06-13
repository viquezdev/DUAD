


function validateInput(number,successCallback,errorCallback){
    if(number>0){
        successCallback(number);
    }
    else{
        errorCallback(number);
    }

}

function successCallback(number){
    console.log("Valid number: ",number);
}

function errorCallback(number){
    console.log("Invalid number: ",number);
}


validateInput(9,successCallback,errorCallback);



