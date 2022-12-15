n=3
arr=[[1,2,3],[4,5,6],[7,8,9]]
# 7 4 1 2 3 6 9 8
result=[]
for i in range(n-1,-1,-1):
    result.append(arr[i][0])
for i in range(1,n):
    result.append(arr[0][i])
for i in range(1,n):
    result.append(arr[i][n-1])
for i in range(n-2,0,-1):
    result.append(arr[n-1][i])
print(result)

# o/p= [7,4,1,2,3,6,9,8]