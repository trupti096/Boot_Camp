# Insertion Sort
# a=[4,2,6,5,7,1]
# for i in range(1,len(a)):
#     key=a[i]
#     j=i
#     while j!=0 and key<a[j-1]:
#         a[j],a[j-1] = a[j-1],a[j]
#         j=j-1
# print(a)




# Recursion
arr=[4,2,6,5,7,1]
n=6
def rec(arr,n):
    if n==len(arr):
        return 
    else:
        for i in range(1,n-1):
            key=arr[i]
            j=i
            if j!=0 and key<arr[j-1]:
                arr[j],arr[j-1]=arr[j-1],arr[j]
                # j=j-1
        return rec(arr,n)
print(arr)