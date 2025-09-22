const data = await getdata();
const newCharList= createAlistFromObject(data);
document.querySelector('#character').appendChild(newCharList);



function createAlistFromObject(obj){
    const ol= document.createElement('ol');
    for (const key in obj){
        if(obj.hasOwnProperty(key)){
            const li =document.createElement('li');
            const value= obj[key];
            if(typeof value == 'object' && value != null){
                li.textContent=`${key}:`;
                li.appendChild(createAlistFromObject(
                Array.isArray(value)?
                value.reduce((acc,cur,i)=> ({...acc,[i]:cur}),{})
                :value
            ));
        }
            else{
                li.textContent=`${key}:${value}`;
            }
        ol.appendChild(li);

        }
    }
    return ol;
}




async function getdata() {
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json'
try{
const response = await fetch(url);
if (!response.ok) {
    throw new Error(`response status : ${response.status}`);
}
const result = await response.json();
return result;
}
 catch(error){
    console.log(error.message)
}
}