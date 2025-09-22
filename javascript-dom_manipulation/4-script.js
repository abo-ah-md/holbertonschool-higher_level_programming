document.getElementById('add_item').addEventListener('click', () => {
  const myList = document.querySelector('.my_list');
  const newItem = document.createElement('li');
  newItem.innerText = 'item';
  myList.appendChild(newItem);
});
