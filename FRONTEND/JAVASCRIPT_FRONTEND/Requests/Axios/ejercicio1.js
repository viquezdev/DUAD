

async function listObjects(){
	try {
		const response = await fetch(`https://api.restful-api.dev/objects`);
		const objects=await response.json();
		const filtered = objects.filter(obj => obj.data);
		filtered.forEach(obj => {
			const details=Object.entries(obj.data).map(([key,value]) =>`${key}: ${value}`).join(", ");
			console.log(`${obj.name} (${details})`);	
			
		});
		
	} catch (error) {
		console.log("error obteniendo datos")
	}
}



listObjects();
