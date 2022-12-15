n=5
k=3
max_len=0
arr=[1,2,2,2,3]
for i in range(0,n):
    for j in range(i,n):
        m=(arr[i:j+1])
        if (sum(m)%k!=0):
            if len(m)>=max_len:
                max_len=len(m)
                count=0
            if len(m)==max_len:
                count+=1
print(count)

# o/p= 1
