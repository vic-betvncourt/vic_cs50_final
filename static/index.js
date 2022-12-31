window.addEventListener('DOMContentLoaded', function(){

    let dogs = document.querySelector("#dogs");
    let selected = document.getElementById("#animal_type");
    let homebtn = document.getElementById("#home-btn")

    selected.addEventListener('change', function(){
        console.log(selected.value);
    }, false);

    homebtn.onclick = function() {
        location.href = "/index.html";
    };
})