# Sub_array
arr=[1,2,3,4]
n=4
result=[]
for i in range(1,2**n):
    # print(bin(i)[2:])
    j=bin(i)[2:]
    j=str(j)
    # print(j)
    
    a=j[::-1]
    print(a)