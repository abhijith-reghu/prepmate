// Wait until the whole page has loaded before running any code
document.addEventListener('DOMContentLoaded', function () {

    // Find the hamburger button and the nav menu by their ID/tag
    const menuToggle = document.getElementById('menu-toggle');
    const nav = document.querySelector('nav');

    // When the hamburger button is clicked...
    menuToggle.addEventListener('click', function () {
        // toggle() adds the "open" class if it's missing, removes it if it's there
        nav.classList.toggle('open');
    });

});
