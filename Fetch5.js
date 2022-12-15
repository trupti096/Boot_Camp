const id = document.querySelector('.id')
const title = document.querySelector('.title')
const price = document.querySelector('.price')
const description = document.querySelector('.description')
const category = document.querySelector('.category')
const image = document.querySelector('.image')
const submitBtn = document.querySelector('.submitBtn')
const container = document.querySelector('.container')


const deleteData = async (dataID) => {
    const response = await fetch(`https://fakestoreapi.com/products/${dataID}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
            // 'Content-Type': 'application/x-www-form-urlencoded',
        },
    })
    getData()
    return response.json()
}

const displayData = (data) => {
    container.innerHTML = ""
    data.map((item, index) => {
        container.innerHTML += `<tr>
        <td>${item.id}</td>
        <td>${item.title}</td>
        <td id="price">${item.price}</td>
        <td>${item.description}</td>
        <td>${item.category}</td>
        <td> <img id ="image" src="${item.image}" alt=""></td>
        <td ><button class="deleteBtn" onclick="deleteData(${item.id})">DELETE</button></td>
        </tr>`
    })

}

const getData = async () => {
    const response = await fetch(`http://localhost:3000/storedata`)

    const data = await response.json()
    console.log(data)
    displayData(data)
}
getData()
const postData = async () => {
    const data = { "id": id.value, "title": title.value, "price": price.value, "description":description.value, "catagory":category.value, "image":image.value }
    const response = await fetch(`http://localhost:3000/storedata`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
            // 'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: JSON.stringify(data)
    })
    getData()
    return response.json()
}
submitBtn.addEventListener('click', postData)


