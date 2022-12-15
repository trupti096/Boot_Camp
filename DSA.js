// console.log('deep') 
// a=[1,2,3,5]
// sum=0
// for (i in a){
//     sum=sum+i}
// sum1=sum(a)
// b=(max(a)*(max(a)+1))//2
// print(b-sum1)


// STACK AND QUEUE


// class Stack{
//     constructor(){
//       this.arr=[]
//     }
//     adding(element){
//       this.arr.push(element)
//     }
//     removing(){
//       return this.isEmpty()? "Stack is empty":this.arr.pop() 
//     }
//     top(){
//       return this.isEmpty()? "Stack is empty":this.arr[this.arr.length-1]
//     }
//     isEmpty(){
//       return this.arr.length==0
//     }
//   }
//   let stack = new Stack
//   stack.adding(10)
//   stack.removing()
//   stack.adding(20)
//   stack.adding(30)
//   console.log(stack)
//   console.log(stack.top())


// STACK=LIFO OR FILO (LAST IN FIRST OUT)
// WE WILL USE PUSH AND POP  

// class Stack{
//     constructor (){
//         this.arr=[]
//     }
//     adding(element){
//         return this.arr.push(element)
//     }
//     removing(element){
//         this.arr.pop()
//     }
//     top(){
//         return this.isEmpty()? 'stack is empty':this.arr[this.arr.length-1]
//     }
//     isEmpty(){
//         this.arr.length==0
//     }
// }
// let stack=new Stack
// stack.adding(10)
// stack.adding(40)
// console.log(stack)
// stack.removing()
// console.log(stack.adding(23))
// console.log(stack)
// stack.top()
// console.log(stack.top())


// // QUEUE -FIFO (FIRST IN FIRST OUT)
// // IF WE ARE USING UNSHIFT THEN WE WILL USE POP TO REMOVE
// // ELSE WE WILL USE PUSH TO ADD OR SHIFT TO REMOVE

// class queue1{
//     constructor(){
//         this.list=[]
//     }
//     adding(element){
//        return this.list.push(element)
//     }
//     remove(element){
//         this.list.shift()
//     }

// }
// let line=new queue1
// line.adding(63)
// line.adding(23)
// console.log(line.adding(56))
// console.log(line.adding(78))
// console.log(line)
// line.remove()
// console.log(line)

// MERGE SORT

// BINARY SEARCH
// time complexity - O(log(n))

// def binary(arr,start,end,number):
//     if start>=end:
        
// arr=[4,2,5,7,3,6,9,0.12]
// number=5
// print(binary(arr,0,len(arr)-1),number)

// def binary(arr,start,end,number):
//     if start>=end:
        
// arr=[4,2,5,7,3,6,9,0.12]
// number=5
// print(binary(arr,0,len(arr)-1),number)


// (question 1)

// for (i=2;i<11;i+=2){
//     console.log(i)
// }

// (question2)

// let a=9;
// for(let i=1;i<11;i++){
//     console.log(a*i)
// }

// (question4)

// let a=[3,4,2,6,7]
// let sum=0;
// for (i=0;i<a.length;i++){
//     sum=sum+a[i]
// }
// console.log(sum)

// (question5)

// let a=[2,5,2,6]
// for(i=a.length-1;i>=0;i--){
//     console.log(a[i])
// }

// (question6)

// let a=[3,4,2,6,7]
// let min=a[0];
// for (i=0;i<a.length;i++){
//     if (min>a[i]){
//         min=a[i]


//     }
    
// }

// (question7)

// b=[]
// function fun1(a){
//     for(i=0;i<a.length;i++){
//         if (a[i]<0){
//             b.push(a[i])
//         }
//     }
//     console.log(b)
// }
// a=[4,8,6,9,-4,6,-3]
// fun1(a)

// (question 8)

// b=''
// a='he  lli o'
// for(i=0;i<a.length;i++){
//     if(a[i]==' '){
//         continue
//     }
//     else{
//         b=b+a[i]
//     }
// }
// console.log(b)

// (question9)


function fun1(a){
     if(a%10==0){
        console.log('true')
     }
     else{
        console.log('false')
     }
}
fun1(18)

// (question10)

