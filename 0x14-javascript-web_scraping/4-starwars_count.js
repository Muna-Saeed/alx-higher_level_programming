#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const filmsData = JSON.parse(body).results;
    const filmsWithWedgeAntilles = filmsData.filter((film) =>
      film.characters.some((character) => character.includes(`/people/${characterId}/`))
    );

    console.log(filmsWithWedgeAntilles.length);
  }
});
