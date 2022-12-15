// const box1=document.querySelector('#name1')
// const box2=document.querySelector('#age1')
// // const box3=document.querySelector('#gender')
// // const box4=document.querySelector('#campus')
// const subbutton=document.querySelector('#submit1')
// alldata=[

// ]

// function deleteRow(index){
//     alldata.splice(index,1);
//     displaydata()
// }
// function displaydata(){
//     tablebody.innerHTML=''
//     alldata.map((item,index)=>{
//         tablebody.innerHTML+=`
//         <tr>
//         <td>${item.name}</td>
//         <td>${item.age}</td>
//         <td> <button onclick='deleteRow(${index})'>delete </button> </td>
//         </tr>
//         `
//     })
// }
// function storedata(){
//     alldata=[...alldata,
//         {
//             'name':box1.value,
//             'age':box2.value
//         }
//     ]
//     displaydata()
// }

// submit1.addEventListener('click',storedata)
// displaydata()

const name = document.querySelector('#name1');
const tableBody= document.querySelector('#tableBody')
let allData = [
    // {
    //     name: 'Maria'
    // }
   
    
];
function editName(index){
   let editedText =  prompt("Enter something")
   allData[index].name =editedText
   displayData()
}
function deleteRow(index){
    allData.splice(index,1);
    displayData()
}
//arr=[a,b,c]==> [...arr,d] ==>[a,b,c,d]
function displayData(){
    tableBody.innerHTML="";
    allData.map((item,index)=>{
        tableBody.innerHTML0=`
        <tr>
        <td>${item.name} <button onclick="editName(${index})">edit</button> </td>
              

      
       <td> <button onclick="deleteRow(${index})">Delete </button> </td>

        </tr>
        `
    })

}
function storeData(){
    allData = [...allData,
        {
            "name": name.value
           
        }
    ];
    // name.value=""
   
    displayData()
}

const submit2 = document.querySelector('#submit1');
submit2.addEventListener('click', storeData)
displayData()