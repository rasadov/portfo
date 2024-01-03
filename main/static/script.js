document.addEventListener('DOMContentLoaded', function () {
    const nav = document.querySelectorAll('.nav-link');
    nav.forEach((card) => {
        card.addEventListener("click", ()=>{
            const NavItem = document.getElementById(card.dataset.nav)
            nav.forEach((c)=>{c.classList.remove("active-link")})
            card.classList.add("active-link")
            document.querySelectorAll(".page-item").forEach((mi) => {mi.classList.add("hidden")})
            NavItem.classList.remove("hidden")
        })
    })

    const get_in_touch = document.querySelector('.nav-link');
    get_in_touch.addEventListener("click", ()=>{
        nav[3].classList.add('active-link')        
    })
})

function checkVisibility_up() {
    const elements = document.querySelectorAll('.fade-in-up');
    elements.forEach(element => {
        const rect = element.getBoundingClientRect();
        const windowHeight = window.innerHeight || document.documentElement.clientHeight;
        
        if (rect.top <= windowHeight * 0.75) {
            element.classList.add('visible');
        }
    });
}

window.addEventListener('scroll', checkVisibility_up);
window.addEventListener('load', checkVisibility_up);

function checkVisibility_right() {
    const elements = document.querySelectorAll('.fade-in-right');
    
    elements.forEach(element => {
        const rect = element.getBoundingClientRect();
        const windowHeight = window.innerHeight || document.documentElement.clientHeight;
        
        if (rect.top <= windowHeight * 0.75) {
            element.classList.add('visible');
        }
    });
}

window.addEventListener('scroll', checkVisibility_right);
window.addEventListener('load', checkVisibility_right);

function checkVisibility_down() {
    const elements = document.querySelectorAll('.fade-in-down');
    
    elements.forEach(element => {
        const rect = element.getBoundingClientRect();
        const windowHeight = window.innerHeight || document.documentElement.clientHeight;
        
        if (rect.top <= windowHeight * 0.75) {
            element.classList.add('visible');
        }
    });
}

window.addEventListener('scroll', checkVisibility_down);
window.addEventListener('load', checkVisibility_down);

function checkVisibility_left() {
    const elements = document.querySelectorAll('.fade-in-left');
    
    elements.forEach(element => {
        const rect = element.getBoundingClientRect();
        const windowHeight = window.innerHeight || document.documentElement.clientHeight;
        
        if (rect.top <= windowHeight * 0.75) {
            element.classList.add('visible');
        }
    });
}

window.addEventListener('scroll', checkVisibility_left);
window.addEventListener('load', checkVisibility_left);
