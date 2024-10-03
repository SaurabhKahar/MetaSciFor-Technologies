document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/items/')
        .then(response => response.json())
        .then(data => {
            const itemsList = document.getElementById('items-list');
            data.forEach(item => {
                const itemDiv = document.createElement('div');
                itemDiv.innerHTML = `<h3>${item.name}</h3><p>${item.description}</p>`;
                itemsList.appendChild(itemDiv);
            });
        })
        .catch(error => console.error('Error fetching items:', error));
});
