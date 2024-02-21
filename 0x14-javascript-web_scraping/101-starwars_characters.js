#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movieData = JSON.parse(body);
    const charactersUrls = movieData.characters;

    // Function to fetch character data and print name
    const fetchAndPrintCharacter = (characterUrl, callback) => {
      request(characterUrl, (characterError, characterResponse, characterBody) => {
        if (characterError) {
          console.error(characterError);
        } else {
          const characterData = JSON.parse(characterBody);
          console.log(characterData.name);
          callback();
        }
      });
    };

    // Use recursion to fetch and print characters in order
    const fetchAndPrintCharactersInOrder = (index) => {
      if (index < charactersUrls.length) {
        fetchAndPrintCharacter(charactersUrls[index], () => {
          fetchAndPrintCharactersInOrder(index + 1);
        });
      }
    };

    fetchAndPrintCharactersInOrder(0);
  }
});
