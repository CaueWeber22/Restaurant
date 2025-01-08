document.getElementById('btn-filter').addEventListener('click', function () {

  const category = document.getElementById('category-select').value;
  const url = new URL(window.location.href);
  if (category) {
       url.searchParams.set('category', category); 
  } else {
      url.searchParams.delete('category'); 
  }
  window.location.href = url.toString(); 
});
