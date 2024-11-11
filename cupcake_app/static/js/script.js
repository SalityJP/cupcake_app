document.getElementById('cupcake-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const name = document.getElementById('name').value;
    const ingredients = document.getElementById('ingredients').value;
    const price = document.getElementById('price').value;

    fetch('/add_cupcake', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `name=${name}&ingredients=${ingredients}&price=${price}`
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        location.reload();  // Recarrega a página para atualizar a lista de cupcakes
    });
});
