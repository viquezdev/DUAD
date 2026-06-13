async function updateUserAddress(id,address){
	try {

		const url='https://httpbin.org/put';

		const userData={
			id:id,
			address:address
		};

		const requestOptions={
			method:"PUT",
			headers:{
				"Content-Type":"application/json"
			},
			body:JSON.stringify(userData)

		};

		const response = await fetch(url,requestOptions);
		console.log(response.status);
		const data=await response.json();
		return data;
		
		
	} catch (error) {
		console.log("error updating address");
		throw error;
	}
}

async function updateUserAndLogData() {
	try {
	const userData= await updateUserAddress(2,'san joaquin de flores');
	console.log(userData);
} catch (error) {
	console.log(error);
}

}

updateUserAndLogData();