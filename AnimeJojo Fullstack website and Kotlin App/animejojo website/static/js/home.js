const header = document.querySelector('.n-header')
const home1 = document.querySelector('.home1')
const searchbox = document.querySelector('#search')
const search = document.querySelector('.search')
const pa = document.querySelector('#popularAnim')
const ta = document.querySelector('#ta')
const la = document.querySelector('#lar')
const hc = document.querySelector('.home1-containerrr')

window.addEventListener('load',()=>{
    setTimeout(() => {
        header.classList.toggle('hide')
        home1.classList.toggle('hide')
    }, 8000);
})

// searchbox.on('key')

// let query = searchbox.value
// console.log(query)


const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Host': 'jikan1.p.rapidapi.com',
		'X-RapidAPI-Key': 'c35ac8900cmsh5ca7846ec59e70dp144bafjsn316847f30361'
	}
};

// if(query){
//     var q = ''
//     q +=  '%' + query.split(' ') + '%'

//     fetch(`https://jikan1.p.rapidapi.com/search/anime?q=${q}`,options)
//         .then(response => response.json())
//         .then((response)=>{
//             console.log(response.results)
//             var result = response.results
//             pa.innerHTML = ''
//             result.forEach(element => {
//                 pa.innerHTML += `
//                 <a href="${element.url}" id="lA">
//                     <img src="${element.image_url}" alt="" id="animeDisplay">
//                     <div id="paTitle">
//                         ${element.title}
//                     </div>
//                 </a>
//                 `
//             });
//         } )
//         .catch(err => console.error(err));
// }
search.addEventListener('submit',(e)=>{
        
    e.preventDefault()
    searcher()

})

function searcher(){

    
    let query = searchbox.value
    console.log(query)
    
    ta.innerHTML = 'Search Results'

    lar.innerHTML = ''
    hc.classList.toggle('hide')
    
    var q = ''
    q +=  '%' + query.split(' ') + '%'
    
    fetch(`https://jikan1.p.rapidapi.com/search/anime?q=${q}`,options)
    .then(response => response.json())
    .then((response)=>{
        console.log(response.results)
        var result = response.results
        pa.innerHTML = ''
        result.forEach(element => {
            pa.innerHTML += `
            <a href="${element.url}" id="lA">
            <img src="${element.image_url}" alt="" id="animeDisplay">
            <div id="paTitle">
            ${element.title}
            </div>
            </a>
            `
        })
    } )
    .catch(err => console.error(err));
    
}


