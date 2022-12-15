const bookID = document.querySelector('.bookID')
const title = document.querySelector('.title')
const author = document.querySelector('.author')
const submitBtn = document.querySelector('.submitBtn')
const container = document.querySelector('.container')

const deleteData = async (dataID) => {
    const response = await fetch(`https://fakestoreapi.com/products${dataID}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        },
    })
    getData()
    return response.json()
}

const getData = async () => {
    const response = await fetch(`https://fakestoreapi.com/products`)
    const data = await response.json()
    console.log(data)
    displayData(data)
}
getData()

const postData = () =>{
    const bodyData= {
        id:itemId.value,
        title:title.value,
        author:author.value
    }
}

