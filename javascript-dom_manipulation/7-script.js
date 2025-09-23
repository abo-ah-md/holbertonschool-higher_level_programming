
async function grapMovies () {
  try {
    const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`ressponse status: ${response.status}`);
    }
    const data = await response.json();
    addMoviesList(data.results);
  } catch (error) {
    console.log(error.message);
  }
}

// a function for adding the list of movies
function addMoviesList (obj) {
  const ol = document.querySelector('#list_movies');
  const fragment = document.createDocumentFragment();
  obj.forEach(movieDetail => {
    const li = document.createElement('li');
    li.textContent = movieDetail.title;
    fragment.appendChild(li);
  });
  ol.appendChild(fragment);
}

grapMovies();
