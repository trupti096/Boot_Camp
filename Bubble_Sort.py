# Bubble Sort
# a=[5,4,2,1,3]
# for i in range(len(a)-1):
#     for j in range(len(a)-1):
#         if a[j] > a[j+1]:
#             a[j],a[j+1] = a[j+1],a[j]
# print(a)

# o/p = [1,2,3,4,5]




# Recursion
arr=[5,4,2,1,3]
n=5
def rec(arr,n):
    for i in range(0,n-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
    if n>0:
        rec(arr,n-1)
rec(arr,n)
print(arr)




# arr=[5,4,2,1,3]
# n=5
# def rec(arr,n):
#     if n==0:
#         return arr
#     else:
#         for i in range(0,n-1):
#             if arr[i]>arr[i+1]:
#                 arr[i],arr[i+1]==arr[i+1],arr[i]
#         return rec(arr,n-1)
# # rec(arr,n)
# print(arr)


# arr=[5,4,2,1,3]
# n=5
# def rec(arr,n):
#     if n==0:
#         return arr
#     else:
#         for i in range(0,n-1):
#             if arr[i]>arr[i+1]:
#                 arr[i],arr[i+1]==arr[i+1],arr[i]
#         return rec(arr,n-1)
# print(arr,0)


