const menuOpen = document.getElementById('menu-open');
const menuClose = document.getElementById('menu-close');
const sideBar = document.querySelector('.container .left-section');
const sidebarItems = document.querySelectorAll('.container .left-section .sidebar .item');

menuOpen.addEventListener('click', () => {
    sideBar.style.top = '0';
});
document.getElementById('getMessageButton').addEventListener('click', function() {
    fetch('http://127.0.0.1:5000/api/message')
        .then(response => response.json())
        .then(data => {
            document.getElementById('message').innerText = data.message;
        })
        .catch(error => console.error('Error:', error));
});
menuClose.addEventListener('click', () => {
    sideBar.style.top = '-60vh';
});

let activeItem = sidebarItems[0];

sidebarItems.forEach(element => {
    element.addEventListener('click', () => {
        if (activeItem) {
            activeItem.removeAttribute('id');
        }

        element.setAttribute('id', 'active');
        activeItem = element;

    });
});