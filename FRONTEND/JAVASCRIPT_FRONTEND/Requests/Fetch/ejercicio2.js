

async function createUser(name,email,password,address){
	try {

		const url='https://httpbin.org/post';

		const userData={
			name:name,
			email:email,
			password:password,
			address:address
		};

		const requestOptions={
			method:"POST",
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
		console.log("error creating user");
		throw error;
	}
}

async function createUserAndLogData() {
	try {
	const userData= await createUser('LUIS VIQUEZ','luis@gmail.com','123456','san joaquin');
	console.log(userData);
} catch (error) {
	console.log(error);
}

}

createUserAndLogData();