const btns = document.querySelectorAll('.info-link')

console.log(btns)

btns.forEach((card) => {
    card.addEventListener("click", ()=>{
        const infoBar = document.getElementById(card.dataset.info)
        btns.forEach((c)=>{c.classList.remove("info-link-active")})
        card.classList.add("info-link-active")
        document.querySelectorAll(".info-link").forEach((mi) => {mi.classList.add("hidden")})
        infoBar.classList.remove("hidden")
    })
})

function checkVisibility_up() {
    const elements = document.querySelectorAll('.fade-in-up');
    console.log(elements)
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
