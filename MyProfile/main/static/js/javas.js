window.onscroll=() => {


let header= document.querySelector('.heder');

header.classList.toggle('sticky',window.scrollY > 100);
}