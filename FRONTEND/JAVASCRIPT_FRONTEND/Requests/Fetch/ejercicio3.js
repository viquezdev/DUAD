

async function getObject(id){
	try {
		const response = await fetch(`https://api.restful-api.dev/objects/${id}`);
		
		if (!response.ok) {
    		throw new Error(`HTTP error: ${response.status}`);
		}
		const data=await response.json();
		return data;
		
		
	} catch (error) {
		console.log("error fetching object");
		throw error;
	}
}

async function fetchObject(id) {
	try {
	const objectData= await getObject(id)
	console.log(objectData);
} catch (error) {
	console.log(error);
}

}

fetchObject(120);