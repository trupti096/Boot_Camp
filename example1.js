// array destructuring
// let obj={
//     name:"Rohit",
//     gender:"male",
//     city:"pune"
// }
// let {name,gender,city}=obj
// console.log(name,gender,city)


// Polimorphisim
// function masterFunction(a,b){
//     return a+b
// }

// function child1(a,b){
//     let c= masterFunction(a,b) + 10
//     console.log(c)
// }
// child1(10,20)



// console.log(masterFunction(20,20))
// console.log(masterFunction(100,200))
// console.log(()=>{

// })




// inheritance

class parentClass{
    constructor(){
        this.name="Trupti"
        this.lastname="Singh"
    }
}
class childClass extends parentClass{
    constructor(firstname,lastname){
        super()
        this.firstname=this.firstname
        this.lastname=this.lastname
    }
}

// let person1 = new parentClass("Trupti","Singh")
let person2 = new childClass("Linu","Singh")
person1.firstname="Tanaya"
console.log(person1)
console.log(person2)



