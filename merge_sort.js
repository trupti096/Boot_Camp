function mergeSort(array){
    if(array.length>1){
        middle=Math.floor(array.length/2)
        left=array.slice(0,middle)
        right=array.slice(middle,array.length)
        mergeSort(left)
        mergeSort(right)
        leftIndex=0
        rightIndex=0
        position=0
        while (leftIndex<left.length && rightIndex<right.length){
            if (left[leftIndex]<right[rightIndex]){
                array[position]=left[leftIndex]
                leftIndex=leftIndex+1
            }
            else{
                array[position]=right[rightIndex]
                rightIndex=rightIndex+1
            }
            position+=1
        }
        while (leftIndex<left.length){
            array[position]=left[leftIndex]
            position=position+1
            leftIndex=leftIndex+1
        }
        while (rightIndex<right.length){
            array[position]=right[rightIndex]
            position=position+1
            rightIndex=rightIndex+1
        }
    }
}
array=[12,4,3,5,1,8,18,2]

mergeSort(array)
console.log(array)

