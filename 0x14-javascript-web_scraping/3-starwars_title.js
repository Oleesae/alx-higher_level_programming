#!/usr/bin/node
/* prints the title of a star wars movie where the episode number
   matches the given integer */
const request = require('request');
const episodeNum = process.argv[2];
const API_URL ='https://swapi-api.hbtn.io/api/films/';

request(API_URL + episodeNum, function (err, response, body) {
    if (err) {
	console.log(err);
    } else if (response.statusCode === 200) {
	const responseJSON.parse(body);
	console.log(responseJSON.title);
    } else {
	console.log('Error code: ' + response.statusCode);
    }
});
