// js del Navbar //
const navToggle = document.querySelector(".nav-toggle");
const navMenu = document.querySelector(".nav-menu");

navToggle.addEventListener("click",() => {
    navMenu.classList.toggle("nav-menu_visible");
});

// Final del js del navar//

// JS Del carousel //
window.addEventListener('load',function()
{
    new Glider(document.querySelector('.carousel-lista'),{
        slidesToShow: 1,
        slidesToScroll: 1,
        
        dots: '.carousel-indicadores',
        arrows: {
        prev: '.carousel-anterior',
        next: '.carousel-siguiente'
        }
    });
});

 // Fin del js del carousel //