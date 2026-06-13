


function readFile(fileName,callback){
    fetch(fileName)
    .then(response=>response.text())
    .then(data=>{
        callback(data);
    });
}


readFile("file1.txt", function(text1) {
    readFile("file2.txt", function(text2) {
        const phrase1 = text1.split(/\s+/);
    const phrase2 = text2.split(/\s+/);
        let words = [];
        for (let i = 0; i < phrase1.length; i++) {
            if (phrase2.includes(phrase1[i])) {
                words.push(phrase1[i]);
            }
        }
        console.log("Mensaje oculto:");
        console.log(words.join(" "));
    });

});