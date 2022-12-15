# Count
num=[1,3,1,3,1,2,3]
i=0
while i<len(num):
    j=0
    count=0
    while j<len(num):
        if (num[i]==num[j]):
            count=count+1
        j=j+1
    if (count>1):
        pass
    else:
        print(num[i])
    i=i+1
