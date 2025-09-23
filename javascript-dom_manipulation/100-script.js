document.addEventListener('DOMContentLoaded', () => {
  const list = document.querySelector('.my_list');

  function addList () {
    const addBtn = document.getElementById('add_item');
    addBtn.addEventListener('click', () => {
      const li = document.createElement('li');
      li.innerText = 'Item';
      list.appendChild(li);
    });
  }

  function removeList () {
    const removeBtn = document.querySelector('#remove_item');
    removeBtn.addEventListener('click', () => {
      if (list.lastElementChild) {
        list.lastElementChild.remove();
      }
    });
  }

  function clearList () {
    const clearBtn = document.querySelector('#clear_list');
    clearBtn.addEventListener('click', () => {
      list.innerHTML = '';
    });
  }

  addList();
  removeList();
  clearList();
});
