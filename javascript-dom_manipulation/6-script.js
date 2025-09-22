async function getdata() {
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json'
try{
const response = await fetch(url);
if (!response.ok) {
    throw new Error(`response status : ${response.status}`);
}
const result = await response.json();
console.log(result)
}
 catch(error){
    console.log(error.message)
}
}
