const box1=document.querySelector('#box1');
const box2=document.querySelector('#box2');
const SubmitBtn1=document.querySelector('#SubmitBtn1')
const SubmitBtn2=document.querySelector('#SubmitBtn2')
const SubmitBtn3=document.querySelector('#SubmitBtn3')
const SubmitBtn4=document.querySelector('#SubmitBtn4')

const addTwoElements=()=>{
    alert(Number(box1.value)+Number(box2.value))
}
SubmitBtn1.addEventListener('click',addTwoElements)

const subTwoElements=()=>{
    alert(Number(box1.value)-Number(box2.value))
}
SubmitBtn2.addEventListener('click',subTwoElements)

const mulTwoElements=()=>{
    alert(Number(box1.value)*Number(box2.value))
}
SubmitBtn3.addEventListener('click',mulTwoElements)


const divTwoElements=()=>{
    alert(Number(box1.value)/Number(box2.value))
}
SubmitBtn4.addEventListener('click',divTwoElements)

