# Sub_array
n=4
# n=5
k=3
s_arr=[]
arr=[2,3,4,5]
# arr=[1,2,2,2,3]
for i in range(0,n):
    for j in range(i,n):
        s_arr.append(arr[i:j+1])
# modified_arr=[]
max_len=0
for i in s_arr:
    if (sum(i)%k!=0):
        # modified_arr.append(i)
        if len(i)>=max_len:
            max_len=len(i)
            count=0
        if len(i)==max_len:
            count+=1
print(s_arr)
# print(modified_arr)
print(count)