# arr=[1,2,3,4]
# # l=len(arr)/2
# # a=arr[:int(l)]
# # b=arr[int(l):]
# # print(a,b)

# size=len(arr)//2
# for i in range(arr,size):
#     print(i)


def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

A = [1,2,3,4,5,6]
B, C = split_list(A)
