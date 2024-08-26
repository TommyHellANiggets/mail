document.addEventListener('DOMContentLoaded', () => {
    const burgerMenu = document.getElementById('burgerMenu');
    const sideMenu = document.getElementById('sideMenu');
    const closeMenu = document.getElementById('closeMenu');

    burgerMenu.addEventListener('click', () => {
        sideMenu.classList.add('menu-open');
    });

    closeMenu.addEventListener('click', () => {
        sideMenu.classList.remove('menu-open');
    });
});
