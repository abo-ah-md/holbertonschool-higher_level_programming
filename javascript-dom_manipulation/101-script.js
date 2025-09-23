document.addEventListener('DOMContentLoaded', () => {
  async function fetchHello (selectedLang) {
    try {
      const url = ` https://hellosalut.stefanbohacek.com/?lang=${selectedLang}`;
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`response status: ${response.status}`);
      }
      const data = await response.json();
      showNewHello(data);
    } catch (error) {
      console.log(error.message);
    }
  }

  function showNewHello (newWord) {
    document.querySelector('#hello').textContent = newWord.hello;
  }

  document.getElementById('btn_translate').addEventListener('click', () => {
    const langselection = document.querySelector('#language_code').value;

    if (!langselection) {
      return;
    }
    fetchHello(langselection);
  });
});
