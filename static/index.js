window.addEventListener('DOMContentLoaded', function(){

    let dogs = document.querySelector("#dogs");
    let selected = document.getElementById("#animal_type");

    selected.addEventListener('change', function(){
        console.log(selected.value);
    }, false);
})