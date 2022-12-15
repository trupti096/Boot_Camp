id1=document.querySelector('#id')
title1=document.querySelector('#title')
price1=document.querySelector('#price')
description1=document.querySelector('#description')
category1=document.querySelector('#category')
container1=document.querySelector('#container')

const deleteData =async(deleteId)=>{
    const r̥esponse=await fetch ( `http://localhost:3000/store/${deleteId}`,{
        method:'DELETE',
        headers:{
            'Content-Type': 'application/json' 
        }
    })
    getData()
}


let displayData=(data)=>{
    container1.innerHTML=''
    data.map((item,idex)=>{
        container1.innerHTML+=`<tr>
        <td> ${item.id}</td>
        <td> ${item.title}</td>
        <td> ${item.price}</td>
        <td> ${item.description}</td>
        <td> ${item.category}</td>
        <td> <button onclick='deleteData(${item.id})'>delete</button></td>
        </tr>`
    })

}

const getData = async () => {
    const response = await fetch('http://localhost:3000/store')
    const data = await response.json()
    console.log(data)
    displayData(data)
}
getData()



const postData=async()=>{
    data={'id':id1.value,'title':title1.value, 'price':price1.value, 'description':description1.value,'category':category1.value}
    const response=await fetch('http://localhost:3000/store' ,
    {
        method:'POST',
        headers:{
            'Content-Type': 'application/json' 
        },
        body:JSON.stringify(data)
    })
    getData()
    return response.json()
}