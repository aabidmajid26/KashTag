document.addEventListener("DOMContentLoaded", ()=>{
    console.log('loaded');
    document.querySelectorAll('a').forEach(function(a){
        a.onclick = function(event){
            event.preventDefault();
            var content = document.querySelector('#content');
            const carousel = document.querySelector('#carousel');
            const player = document.querySelector('#player_info');
            player.style.display = 'none';
            const Id = a.getAttribute('id');
            const activity = a.dataset.activity;
            if (Id === 'home-link' || Id=== 'home-link1'){
                carousel.style.animationPlayState = 'paused';
                carousel.style.display = 'block';
                content.style.display = 'none';
            }
            else if (Id === 'links'){
                content.style.display = 'block';
                fetch(`display/${activity}`)
                .then(response => response.json())
                .then(json => {
                    const len = json.length;
                    var box_count = 0;
                    console.log(json.Id);
                    content.innerHTML = '';
                    while (box_count<len){
                        var row = document.createElement('div');
                        row.setAttribute('class', 'row');
                        var i;
                        for (i=0;i<3;i++){
                            const a = document.createElement('a')
                            const box = document.createElement('div');
                            a.setAttribute('href', '#');
                            a.setAttribute('class', 'col-sm');
                            a.setAttribute('id', 'dabba');
                            a.setAttribute('data-activity', activity);
                            a.setAttribute('data-id', json[box_count].Id);
                            a.innerHTML = `<h5>${json[box_count].name}</h5>`;
                            a.appendChild(box);
                            row.appendChild(a);
                            box_count++;
                            if (box_count>=len){break;}
                        }
                        content.appendChild(row)

                    }
                    carousel.style.animationPlayState = 'running';
                    document.addEventListener("animationend",()=>{
                    carousel.style.display = 'none';
                    carousel.style.animationPlayState = 'paused';
                    });
                    document.querySelectorAll('#dabba').forEach(function(box){
                        box.onclick = function(event){
                            event.preventDefault();
                            const activity1 = box.dataset.activity;
                            const Id1 = box.dataset.id;
                        
                            console.log(activity1, Id1, typeof(Id1));
                            const player = document.querySelector('#player_info');
                            content.style.display='none';
                            player.style.display = 'block';
                            if (activity1 === 'hut' || activity1==='hotel' || activity1==='ski-shop'||activity1==='ski'){
                                player.innerHTML = "Hotel Info";
                            }else{
                                //do this
                                player.innerHTML = "People Info";
                            }
                        }
                    });

                });
            }
        }
    });

    });