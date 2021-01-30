document.addEventListener("DOMContentLoaded", ()=>{
    console.log('loaded');
    document.querySelectorAll('a').forEach(function(a){
        a.onclick = function(event){
            event.preventDefault();
            var content = document.querySelector('#content');
            const carousel = document.querySelector('#carousel');
            const people = document.querySelector('#people_info');
            people.style.display = 'none';
            const Id = a.getAttribute('id');
            const activity = a.dataset.activity;
            if (Id === 'home-link' || Id=== 'home-link1'){
                carousel.style.animationPlayState = 'paused';
                carousel.style.display = 'block';
                content.style.display = 'none';
                people.style.display = 'none';
            }
            else if (Id === 'links'){
                content.style.display = 'block';
                fetch(`display/${activity}`)
                .then(response => response.json())
                .then(json => {
                    if (activity==='hut'||activity==='hotel' ||activity==='ski'||activity==='ski-shop'){
                        createPageForInanimate_List(json, content, activity)
                        disappearCarousel(carousel);
                        people.style.display = 'none';
                    }
                    else if (activity==='sledge' || activity==='instructor' || activity==='ski-lender'){
                        
                        people.style.display = 'block';
                        createPageForPeople(json, people, activity)
                        disappearCarousel(carousel);
                        content.style.display = 'none';
                    }
                    document.querySelectorAll('#dabba').forEach(function(box){
                        box.onclick = function(event){
                            event.preventDefault();
                            const activity1 = box.dataset.activity;
                            const Id1 = box.dataset.id;
                            const people = document.querySelector('#people_info')
                            content.style.display='none';
                            player.style.display = 'block';
                            
                        }
                    });

                });
            }
        }
    });

    });


function createPageForInanimate_List(json,content, activity){
    const len = json.length;
    var box_count = 0;
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
        content.appendChild(row);

        }
}

function createPageForPeople(json, people, activity){
    len = json.length;
    var i;
    const tbody = people.querySelector('tbody');
    console.log(json)
    for(i = 0; i<len; i++){
        const fid = json[i].Id
        


        const tr = document.createElement('tr');
        const td1 = document.createElement('td');
        const td2 = document.createElement('td');
        const th = document.createElement('th');
        td1.innerText = json[i].name;
        th.innerText = i+1;
        th.setAttribute('scope', 'row');

        fetch(`getphone/${activity}/${fid}`)
        .then(response => response.text())
        .then(text => {
            const pn = text;
            td2.innerText = pn;
            
        });

        tr.appendChild(th);
        tr.appendChild(td1);
        tr.appendChild(td2);
        tbody.appendChild(tr);
    }
}

function disappearCarousel(carousel){

    carousel.style.animationPlayState = 'running';
    document.addEventListener("animationend",()=>{
    carousel.style.display = 'none';
    carousel.style.animationPlayState = 'paused';
    });
}