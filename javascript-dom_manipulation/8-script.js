
async function fetchWord () {
  try {
    const response = await fetch('https://hellosalut.stefanbohacek.com/?lang=fr');
    if (!response.ok) {
      throw new Error(`response status: ${response.status}`);
    }
    const data = await response.json();
    addWord(data);
  } catch (error) {
    console.log(error.message);
  }
}

function addWord (word) {
  const hello = document.getElementById('hello');
  hello.innerText = `${word.hello}`;
}

document.addEventListener('DOMContentLoaded', () => {
  fetchWord();
});
