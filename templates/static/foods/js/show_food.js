document.getElementById('btn-filter').addEventListener('click', function () {
  console.log("Chamou")
  const category = document.getElementById('category-select').value; // Obtém o valor selecionado
  const url = new URL(window.location.href);
  if (category) {
       url.searchParams.set('category', category); // Define o parâmetro 'category'
  } else {
      url.searchParams.delete('category'); // Remove o parâmetro se "Todos" estiver selecionado
  }
  window.location.href = url.toString(); // Redireciona para a URL com o parâmetro
});
