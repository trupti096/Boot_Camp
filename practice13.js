const box = document.querySelector('.box');
const submitBtn = document.querySelector('.submitBtn');
const container = document.querySelector('.container')
const calculateResult=()=>{
    container.inerHTML=""
    let resultString=box.value.toLowerCase()
    let newString=""
    for (let i=0;i<resultString.length;i++){
        if (resultString[i]==" "){
            newString+=resultString[i+1].toUpperCase()
            i+=1
        }
        else{
            newString+=resultString[i]
        }
    }
    alert(newString)
    container.innerHTML+='<h1>$(newString}</h1>'
}
submitBtn.addEventListener('click',calculateResult)