

const getUserData = async () => {
	console.log("Requesting data...");
	const response = await fetch(`https://api.restful-api.dev/objects`);
	const data = await response.json();
	return data;
}





getUserData().then(data => {
   
    const filtered = objects.filter(obj => obj.data);
   
    console.log(filtered);
});