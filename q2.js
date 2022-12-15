let a=[5,3,4,1,2];
for (let i=0; i<a.length;i++){
    key=a[i]
    j=i
    while (j!=0 && key<a(j)){
        temp=a[i]
        a[i]=a[j]
        a[j]=temp
        j=j-1
        key=a[j]
    }
    console.log(a);
}