document.addEventListener('click', function(event) {
    const dropdowns = document.querySelectorAll('.dropdown-content');

    dropdowns.forEach(dropdown => {
        // Verifica se o clique foi feito fora do dropdown e fecha-o
        if (!event.target.closest('.dropdown')) {
            dropdown.style.display = 'none';
        }
    });

    // Verifica se o clique foi nos três pontinhos e abre o dropdown correspondente
    if (event.target.classList.contains('three-dots')) {
        const content = event.target.nextElementSibling;
        content.style.display = 'block';
    }
});