const headerButton = document.getElementById('toggle_header');
const header = document.querySelector('header').classList;
headerButton.addEventListener('click', () => {
  header.toggle('green');
  header.toggle('red');
});
