# Selection Sort
# a=[5,4,3,2,1]
# for i in range(len(a)-1):
#     min=i
#     for j in range(i+1,len(a)):
#         if a[i] > a[j]:
#             min=j
#         a[i],a[min]=a[min],a[i]
# print(a)

# # o/p = [1,2,3,4,5]




# Recursion
arr=[5,4,3,2,1]
def selection(arr,result):
    if len(arr)==0:
        return " "
    else: 
        j=arr.index(min(arr))
        arr[0],arr[j]=arr[j],arr[0]
        result.append(arr[0])
        return selection(arr[1:],result)
# arr=[5,4,3,2,1]
result=[]
selection(arr,result)
print(result)
    
    
    
# arr=[5,4,3,2,1]
# def selection(arr,result):
#     if len(arr)==0:
#         return " "
#     else: 
#         j=arr.index(min(arr))
#         arr[0],arr[j]==arr[j],arr[0]
#         result.append(arr[0])
#         return selection(arr[1:],result)
# result=[]
# selection(arr,result)
# print(result)