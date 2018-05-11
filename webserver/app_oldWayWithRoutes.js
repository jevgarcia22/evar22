const express = require('express');

const app = express();

app.get('/', function(req, res){
	res.send('This is the home page');
});

//this is exactly the same, but uses ES6 syntax
app.get('/about', (req, res) => {
	res.send('<h1>This page injects html directly into the request</h1>');
});

app.get('/users/:name', (req, res) => {
	let user = req.params.name;
	res.send('<h1> This page takes in a route parameter. Here, the parameter is ' +user +'</h1>');
});

app.listen(3000, function(){
	console.log('Server started on port 3000....');
});