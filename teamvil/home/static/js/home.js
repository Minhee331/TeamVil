const slide_list = document.querySelectorAll('.home-slide-item');
const dot = document.querySelectorAll('.home-slide-dot');

let counter = 1;
slidefunc(counter);

let timer = setInterval(autoslide, 5000);
function autoslide(){
    counter += 1;
    slidefunc(counter);
}

function plusSlide(n){
    counter += n;
    slidefunc(counter);
    resetTimer();
}

function currentSlide(n){
    counter = n;
    slidefunc(counter);
    resetTimer();
}

function resetTimer(){
    clearInterval(timer);
    timer = setInterval(autoslide, 5000)
}

function slidefunc(n){
    let i;
    for(i=0; i<slide_list.length; i++){
        slide_list[i].style.display = "none";
    }
    for(i=0; i<dot.length; i++){
        dot[i].classList.remove("active-slide");
    }
    if(n > slide_list.length){
        counter = 1;
    }
    if(n < 1){
        counter = slide_list.length;
    }
    slide_list[counter-1].style.display = "block";
    dot[counter-1].classList.add('active-slide');
}

