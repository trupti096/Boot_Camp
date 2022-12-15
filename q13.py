n=[1, 1, 1, 1, 2, 3]
i=0
c=0
e=[]
while i<len(n):
    c=c+1
    d=c//2
    j=0
    c1=0
    while j<len(n):
        if (n[i]==n[j]):
            c1=c1+1
        j=j+1
    if n in e:
        e.append(n[i])
if c>d:
    print(c)
else:
    print(-1)
    i=i+1
    # if n[i]>d:
    #     print(n)
    #     # pass
    # else:
    #     print("-1")
    # i=i+1