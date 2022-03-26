const authentication = document.querySelector('.authentiation')
const head = document.querySelector('.headd')
const hero = document.querySelector('.hero')

window.addEventListener('load',()=>{
    setTimeout(() => {
        authentication.classList.toggle('hide')
        head.classList.toggle('hide')
    }, 7000);
})