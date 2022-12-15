// let API =`https://fakestoreapi.com/products`
// let data = async()=>{
//     let response = await fetch(API)
//     let result = await response.json()
//     console.log(result)
// }
// data()


container1=document.querySelector('#container')
let sortButton=document.querySelector('#sortButton')
let unsortButton=document.querySelector('#unsortButton')


const displayData=(data)=>{
    // container1.innerHTML=''
    data.map((item,index)=>{
        container1.innerHTML+=`<div>
        <h1>${item.title}</h1>
        <img src=${item.image} />let
        <p>${item.description}</p>
        <button>$${item.price}</button>
         </div>
        `
    })
}

const callApi=async()=>{
    const response= await fetch(`https://fakestoreapi.com/products`)
    const data=await response.json()
    console.log(data)
    displayData(data)
}
callApi()

const sortPrice=async()=>{
    const response= await fetch(`https://fakestoreapi.com/products`)
    const data=await response.json()
    data.sort((a,b)=>{
        return a.price - b.price;
    });
    console.log(data)
    displayData(data)
}
sortPrice()


const unsortPrice=async()=>{
    const response= await fetch(`https://fakestoreapi.com/products`)
    const data=await response.json()
    console.log(data)
    displayData(data)
}
unsortPrice()


let sortBool=false
sortBool?sortButton.addEventListener('click',unsortPrice):sortButton.addEventListener('click',sortPrice)
sortButton.addEventListener('click', () =>{
    sortBool=!sortBool
    container1.innerHTML=""
    displayData()
})

