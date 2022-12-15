# arr=[31,34,71,82,81,91,33,11,1,3]
# i=0
# count=0
# sum=0
# # while i<len(arr):
# #     j=0
# #     while j<len(arr):
# #         a=arr[i]%10
# #         b=a[i]//10
# #         c=c+1
# #     j=j+1
# # print(b)
# # i=i+1


# for i in range(len(arr)):
#     for j in range(len(arr)):
#         count=count+1
#         a=arr%10
#         b=a[i]//10
    
# print(count)


arr=[31,34,71,82,81,91,33,11,1,3]
a=[0,0,0,0,0,0,0,0,0,0]
sum=0
for i in arr:  
    a[i%10] += 1
print (a)