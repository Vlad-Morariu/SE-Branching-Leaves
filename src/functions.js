fetch('b2.json')
  .then(response => response.json())
  .then(data => {
    const container = document.getElementById('checkbox-container');

    data.forEach(option => {
      const checkbox = document.createElement('input');
      checkbox.type = 'checkbox';
      checkbox.id = option.id;
      checkbox.name = 'options';
      checkbox.value = option.id;

      const author = document.createElement('author');
      author.textContent = b2.author;
      author.setAttribute('for', option.id);

      container.appendChild(checkbox);
      container.appendChild(author);
    });
  })
  .catch(error => {
    console.error(error);
  });
