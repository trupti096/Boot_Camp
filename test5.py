n=int(input("enter a no = "))
k=int(input("enter a no = "))
v=int(input("enter a no = "))
a=int(input("enter a no = "))
b=a
x=((v*(n+k))-b)/k
if(x>0 and ((v*(n+k))-b)%k==0):
    print(int(x))
else:
    print("-1")