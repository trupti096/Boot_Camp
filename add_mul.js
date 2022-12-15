const box1=document.querySelector('#number1')
const box2=document.querySelector('#number2')
const add1=document.querySelector('#submit1')
// const sub1=document.querySelector('#submit2')
// const mul1=document.querySelector('#submit3')
// const div1=document.querySelector('#submit4')

const data1=()=>{
    alert(Number(box1.value)+Number(box2.value))
}
submit1.addEventListener('click',data1)

const data2=()=>{
    alert(Number(box1.value)-Number(box2.value))
}
submit2.addEventListener('click',data2)

const data3=()=>{
    alert(Number(box1.value)*Number(box2.value))
}
submit3.addEventListener('click',data3)

const data4=()=>{
    alert(Number(box1.value)/Number(box2.value))
}
submit4.addEventListener('click',data4)