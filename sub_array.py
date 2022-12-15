# Sub Array
# arr=[1,2,3,4,5,6]
# n=6
# result=[]
# for i in range(1,2**n):
#     a=str(bin(i)[2:][::-1])
#     # print(a)
#     temp_arr=[]
#     for i in range(0,len(a)):
#         if a[i]=="1":
#             temp_arr.append(int(arr[i]))
#     result.append(temp_arr)
# print(result)




# Recursion
arr=[1,2,3]
def rec(arr,start,end):
    if len(arr)==end:
        return 
    elif start>end:
        return rec(arr,0,end+1)
    else:
        print(arr[start:end+1])
        return rec(arr,start+1,end)
# arr=[1,2,3]
print (rec(arr,0,0))