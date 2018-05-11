const express = require('express');
const path = require('path');

const app = express();

// set static path for express to look for
app.use(express.static(path.join(__dirname, 'public')));

app.get('/users', (req, res) => {
	let users = [
		{
			first_name: "John",
			last_name: "Doe",
			age: 34,
			gender: "male"
		},
		{
			first_name: "Tom",
			last_name: "Jackson",
			age: 23,
			gender: "male"
		},
		{
			first_name: "Tracy",
			last_name: "Smith",
			age: 38,
			gender: "female"
		},
	];
	
	res.json(users);
});

app.listen(3000,() => {
	console.log('Server started on port 3000....');
});