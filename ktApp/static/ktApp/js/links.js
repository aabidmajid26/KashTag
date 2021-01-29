document.addEventListener("DOMContentLoaded", ()=>{
    console.log('loaded');
    document.querySelectorAll('a').forEach(function(a){
        a.onclick = function(event){
            event.preventDefault();
            const content = document.querySelector('#content');
            const carousel = document.querySelector('#carousel');
            if (a.dataset.activity === 'ski'){
                carousel.style.animationPlayState = 'running';
                document.addEventListener("animationend",()=>{
                    carousel.style.display = 'none';
                    carousel.style.animationPlayState = 'paused';
                });
                content.innerHTML = '<h1>Hello Skier</h1>';
            }
            else if (a.dataset.activity === 'sledge'){
                content.innerHTML = '<h1>Hello Sledger</h1>';
                carousel.style.animationPlayState = 'running';
                document.addEventListener("animationend",()=>{
                    carousel.style.display = 'none';
                    carousel.style.animationPlayState = 'paused';
                });
            }
            else if (a.dataset.activity === 'ski-lender'){
                content.innerHTML = '<h1>Hello Ski-Lender</h1>';
                carousel.style.animationPlayState = 'running';
                document.addEventListener("animationend",()=>{
                    carousel.style.display = 'none';
                    carousel.style.animationPlayState = 'paused';
                });
            }
            else if (a.dataset.activity === 'ski-shop'){
                content.innerHTML = '<h1>Hello Ski-Shopper</h1>';
                carousel.style.animationPlayState = 'running';
                document.addEventListener("animationend",()=>{
                    carousel.style.display = 'none';
                    carousel.style.animationPlayState = 'paused';
                });
            }
            else if (a.dataset.activity==='home'){
                content.innerHTML = '';
                carousel.style.display = 'block';
            }
            else if (a.dataset.activity === 'ski-instructor'){
                content.innerHTML = '<h1>Hello Ski-Instructor</h1>';
                carousel.style.animationPlayState = 'running';
                document.addEventListener("animationend",()=>{
                    carousel.style.display = 'none';
                    carousel.style.animationPlayState = 'paused';
                });
                
            }
            else if (a.dataset.activity === 'hut'){
                content.innerHTML = '<h1>Hello Hutter</h1>';
                carousel.style.animationPlayState = 'running';
                document.addEventListener("animationend",()=>{
                    carousel.style.display = 'none';
                    carousel.style.animationPlayState = 'paused';
                });
                
            }
            else if (a.dataset.activity === 'hotel'){
                content.innerHTML = '<h1>Hello Hotelier</h1>';
                carousel.style.animationPlayState = 'running';
                document.addEventListener("animationend",()=>{
                    carousel.style.display = 'none';
                    carousel.style.animationPlayState = 'paused';
                });
            }
        }
    })
});