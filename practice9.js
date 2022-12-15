const name = document.querySelector('.name');
const gender = document.querySelector('.gender');
const age = document.querySelector('.age');
const campus = document.querySelector('.campus');
const tableBody = document.querySelector('.tableBody')

let allData = [];

function storeData(){
    allData=[...allData,
        {
            "name": name.value,
            "gender": gender.value,
            "age": age.value,
            "campus": campus.value,
        }
    ];
    console.log(allData)

}