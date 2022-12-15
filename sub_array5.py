# Sub_array
n=4
arr=[1,2,3,4,5,6]
result=[]
for i in range(0,n):
    for j in range(i,n):
        result.append(arr[i:j+1])
print(result)