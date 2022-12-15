num=[1,2,3,4,2,1,6,5]
i=0
e=[]
while i<len(num):
    if num[i] not in e:
        e.append(num[i])
    i=i+1
# print(e)
j=0
while j<len(e):
    k=0
    while k<len(e):
        if e[j]<e[k]:
            e[j],e[k]=e[k],e[j]
        k=k+1
    j=j+1
print(e)




# f=[]
# l=0
# while l<len(e):
#     m=0
#     max1=0
#     while m<len(e):
#         if e[i]>max1:
#             max1=e[j]
#             m=m+1
#     e.remove(max1)
#     f.append(max1)
#     l=l+1
# print(f)





# # set
# obj={}
# for i in range(0,6):
#     if obj[i]+1:
        
        
        
        
