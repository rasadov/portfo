document.addEventListener('DOMContentLoaded', function () {
    const about = document.querySelectorAll('.edit');
    about.forEach((card) => {
        card.addEventListener("click", ()=>{
            const infoBar = document.getElementById(card.dataset.edit)
            about.forEach((c)=>{c.classList.remove("edit-active")})
            card.classList.add("edit-active")
            document.querySelectorAll(".edit-card").forEach((mi) => {mi.classList.add("hidden")})
            infoBar.classList.remove("hidden")
        })
    })
})



function openModal() {
    document.getElementById("myModal").style.display = "flex";
}

function closeModal() {
    document.getElementById("myModal").style.display = "none";
}