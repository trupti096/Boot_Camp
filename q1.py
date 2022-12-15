a=[4,2,6,5,7,1] 
for i in range(1,len(a)):   
    key=a[i]
    j=i-1
    while j>=0 and key<a[j]:
        a[j+1]=a[j]
        j=j-1
    a[j+1]=key
print(a)

# o/p= [1,2,4,5,6,7]