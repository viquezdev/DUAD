function getPokemon(id) {
  return fetch(`https://pokeapi.co/api/v2/pokemon/${id}`)
    .then(res => res.json())
    .then(data => data.name);
}

const pokemon1 = getPokemon(1);
const pokemon2 = getPokemon(4);
const pokemon3 = getPokemon(7);

Promise.any([
  getPokemon(1),
  getPokemon(4),
  getPokemon(7)
])
.then(names => {
  console.log(names);
});