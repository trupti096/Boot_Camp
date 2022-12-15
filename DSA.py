# a=[7,6,8,6,5,9]
# b=[]
# for i in a:
#     c=0
#     for j in a:
#         if i==j:
#             c=c+1
#     if i not in b:
#         if c>1:
#             b.append(i)
# print(b)

# a=[7,6,8,6]
# b=a [::-1]
# print(b)
# print(min(9,8)) 

# a=[10,7,9,5,7,10,7,11,7,10,2]
# b={}
# for i in a:
#     c=0
#     for j in a:
#         if i==j:
#             c=c+1
#     b[c]=i
# print(b)
# max=0
# for k in b:
#     if max <k:
#         max=k
# print(b[max])

# a=[2,4,6,8]
# b=[1,3,5,7,9]
# for i in b:
#     a.append(i)
# print(a)
# c=0
# for i in a:
#     c=c+1
# print(c)
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]>a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)

# a=5
# arr=['even','odd']
# print(arr[a%2==0])

# BUBBLE SORT

# a=[5,4,8,7,3]
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]>a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)


# SELECTION SORT

# a=[5,4,3,2,1]
# for i in range(len(a)):
#     min=i
#     for j in range(i+1,len(a)):
#         if a[min]>a[j]:
#             min=j
#     temp=a[i]
#     a[i]=a[min]
#     a[min]=temp
#     # or a[i],a[min]=a[min],a[i] 
# print(a)

# INSERTION SORT
# a=[9,6,8,3,1,5]
# for i in range(len(a)):
#     key=a[i]
#     j=i
#     # for j in range(j=i,len(a),-1):
#     while j!=0 and key<a[j-1]:
#         a[j-1],a[j]=a[j],a[j-1]
#         j-=1
#         key=a[j]
#         # if a[i-1]>a[j]:
# print(a) 

# ARRAY ASSIGNMENT
# a=[7,3,10,6,5]
# k=3
# for i in range(len(a)):
# T=int(input())
# for i in range(T):
#     c=0
#     L,R=map(int,input().split())
#     for j in range(L,R+1):
#         if j%10==2 or j%10==3 or j%10==9:
#             c=c+1
#     print(c)

# a=list(int(input()))
# b=list(a)
# a=2333
# c=list(str(a))
# print(len(a))
# print(c)
# c=567
# c=list(str(c))
# for i in range(len(c)):
#     print(c[i])
# a=list(input())
# a=334
# b=str(a)
# if '0' in b or '5' in b:
#     print('yes')
# else:
#     print('no')
# print(a)


# arr=[6,2,5,5,4,5]
# a,b=map(int,input().split())
# c=a+b
# e=0
# d=str(c)
# for i in d:
#     j=int(i)
#     e=e+arr[j]
# print(e)

# FACTORIAL
# L=[]
# for i in range(1,11):
#     if i==1:
#         L.append(i)
#     else:
#         a=L[-1]*i 
#         L.append(a)
# print(L)

# FEBONACCI SERIES

# a=[0,1]

# for i in range(5):
#     if i==0:
#         pass
#     else:
#         b=a[-1]+a[-2]
#         a.append(b)
# print(a)

# OR

# FEBONACCI SERIES

# a=[0,1]
# for i in range(1,5):
#     b=a[-1]+a[-2]
#     a.append(b)
# print(a)

# given no is power of 2 or not

# a=16
# for i in range(1,a):
#     if 2**i==a:
#         print('yes')
#         break
#     else:
#         pass

# print(Math.log(16))

# how many no are power of 2 
# a=[2]
# while a[-1]<=16:
#     if a[-1]==16:
#         break
#     else:
#         a.append(a[-1]*2)
# print(a)


# find the missing no in Series

# a=[1,2,3,5]
# sum1=sum(a)
# b=(max(a)*(max(a)+1))//2
# print(b-sum1)


# 4+3+(2*i)
# o/p=[1,4,9,16,25,36,49,64,81.......]
# a=[1]
# for i in range(99):
#         a.append(a[-1]+3+(2*i))
# print(a)

# a=[31,19,21,35,36,9,7,1]
# b=[-1]
# for i in range(1,len(a)):
#     if a[i-1]<a[i]:
#         b.append(a[i])
#     else:
#         b.append(-1)
# print(b)


# a=[['*','1','*'],['1','*','1'],['*','1','*']]
# h=0
# v=0
# for r in range(len(a)):
#     if a[0][r]==a[len(a)-1][r]:
#         h=h+1
#     if a[r][0]==a[r][len(a)-1]:
#         v=v+1
# if h==len(a) and v==len(a):
#     print('both')
# elif h==len(a):
#     print('horizontal')
# else:
#     print('vertical')

# ab=['a'=='z','b'=='y']
# print(ab[0])
# a=input()
# for i in range(len(a)):
#     print(a[i])
# a=['a','b']
# if 'a'==0 or 'b'==0:

#     a['a']-a[1]
# print(3//2)

# import Math

# a=7/2
# print(Math.ceil(a))

# if s1[i]>s2[i]:
#     c=26-z-a
# else:
#     c=a-b

# T=int(input())
# for i in range(T):
#     l=0
#     N=int(input())
#     A=input()
#     B=input()
#     s={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
#     for i in range(N):
#         if A[i]<B[i]:
#             l=l+26-s[A[i]]-s[B[i]]
#         else:
#             l=l+s[A[i]]-s[B[i]]
#     print(l)

#  2 QUESTION

# T=int(input())
# for i in range(T):
#     N=int(input())
#     d=0
#     p=[]
#     A=list(map(int,input().split()))
#     for i in A:
#         c=0
#         for j in A:
#             if i==j:
#                 c=c+1
#         if c>1:
#             pass  
#         else:
#             print(i)
# print(d)

# 1 QUESTION

# N=int(input())
# A=map(int,input().split())
# d=set(A)
# print(d)
# l=list(d)
# s=l.sort()
# print(l)
# if len(l)<3:
#     print('not possible')
# else:
#     min=l[0:3]
#     max=l[len(l)-3:len(l)]
#     print(min)
#     print(max)


# 3 QUESTION

# K=map(int,input().split())


# k=3
# N=list(map(int,input().split()))
# s=[]
# for i in range(0,len(N)):
#     for j in range(i,len(N)):
#         s.append(N[i:j+1])
# print(s)
# c=0
# m=[]
# for i in s:
#     if sum(i)%k!=0:
#         m.append(i) 
# print(m)
# max=len(m[0])
# c=0
# for j in m:
#     if max<len(j):
#         max=len(j)
#         c=c+1
# print(max,c)

# 4 QUESTION

# [1  2  3 4
# 5  6  7  8
# 9 10 11 12
# 13 14 15 16]


# o/p   7 4 1 2 3 6 9 8

# a=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# s=[]
# for i in range(len(a)-1,-1,-1):
#     s.append((a[i][0]))
# for j in range(1,len(a)):
#     s.append(a[0][j])
# for k in range(1,len(a)):
#     s.append(a[k][len(a)-1])
# for l in range(len(a)-2,0,-1):
#     s.append(a[len(a)-1][l])
# print(*s,sep=' ')


# 5 QUESTION

# [1  2  3 4
# 5  6  7  8
# 9 10 11 12
# 13 14 15 16]

# 13 14 15 16 12 8 4 3 2 1 5 9 10 11 7 6

# or (n*k)%9
# if remainder is 0 then ans is 9

# n=142
# k=3
# a=str(n)*3
# b=list(a)
# print(a)
# while int(a)>9:
#     sum=0
#     for i in str(a):
#         sum=sum+int(i)
#     a=sum
# print(sum) 

# DOC 1

# T=9
# N=[1,2,3,4]
# m=''
# for i in N:
#     while
#     if i >=1:
#         a=i//2
#         m=m+str(i%2)
#     print(m)

# s=[]
# for i in range(0,len(N)):
#     for j in range(i,len(N)):
#         s.append(N[i:j+1])
# print(s)
# l=[]
# for j in s:
#     a=sum(j)
#     if a==5:
#         l.append(j)
# print(l)

# QUESTION 1

# a=[1,2,2,2,2,3]
# s={}
# for i in a:
#     c=0
#     if i not in s:
#         for j in a:
#             if i==j:
#                 c=c+1
#         s[i]=c
# print(s)
# res=False
# for i in s:
#     if s[i]>len(a)//2:
#         print(i,end='' )
#         res=True
# if res==False:
#     print(-1)

# 2 QUESTION

#  CONTINUOUS SUBARRAY

# a=[1,2,1,2,1]
# s=[]
# for i in range(len(a)):
#     for j in range(i,len(a)):
#         s.append(a[i:j+1])
# print(s)
# d={}
# for i in s:
#     for j in range(len(s)):
#         if len(i)==j:
#             d[j]=i
# print(d)


# RECURRSION OF FACTORIAL

# def recurrsion(a):
#     if a==1:
#         return 1
#     else:
#         return a*recurrsion(a-1)
# print(recurrsion(5))


# RECURRSION OF FEBONACCI SERIES

# def recurrsion(n,a,b):
#     if a==1:
#         return 1
#     else:
#         return a*recurrsion(a-1)
# print(recurrsion(5,0,1))

# FIND THE SUBARRAY

# arr=[1,2,3]
# n=3
# result=[]
# for i in range(0,2**n):
#     a=str(bin(i)[2:][::-1])
#     print(a)
#     temp=[]
#     for i in range(0,len(a)):
#         if a[i]=='1':
#             temp.append(int(arr[i]))
#         result.append(temp)
# print(result)  


# a=[32,34,77,82,81,91,33,11,3,1]
# c1,c2,c3,c4,c5,c6,c7,c8,c9=0,0,0,0,0,0,0,0,0
# for i in a:
#     if i%10==1:
#         c1+=1
#     elif i%10==2:
#         c2+=1
#     elif i%10==3:
#         c3+=1
#     elif i%10==4:
#         c4+=1
#     elif i%10==5:
#         c5+=1
#     elif i%10==6:
#         c6+=1
#     elif i%10==7:
#         c7+=1
#     elif i%10==8:
#         c8+=1
#     elif i%10==9:
#         c9+=1
# print(c1,c2,c3,c4,c5,c6,c7,c8,c9)
# sum=c1+c2+c3+c4+c5+c6+c7+c8+c9
# print(sum)

# OR

# a=[32,34,77,82,81,91,33,11,3,1]
# a1=[0,0,0,0,0,0,0,0,0]
# for i in a:
#     a1[i%10]+=1
# print(a1)



# ASSIGNMENT ON 5TH NOVEMBER

# QUESTION NO 1
# 2
# 7
# 100 80 60 70 60 75 85
# 5
# 3 5 0 9 8
# Sample Output 1
# 1 1 1 2 1 4 6
# 1 2 1 4 1

# a=[100,80,60,70,60,75,85]
# a=[100 ,60 ,70 ,65 ,80 ,85]
# a=[3,5,0,9,8]
# s=''
# for i in range(len(a)):
#     if i==0:
#         s=s+' '+'1'
#     elif a[i]>a[i-1]:
#         c=1
#         for j in range(i,0,-1):
#             if a[i]>a[j-1]:
#                 c=c+1
#             else:
#                 break 
#         s=s+" "+str(c)
#     else:
#         s=s+" "+str(1)
# print(s)


# QUESTION NO 3
# a=math.ceil(5/2)

# for i in range(1,6,2):
#     print(i)

# FACTORIAL OF RECURSSION

# def a(n):
#     if n==1:
#         return 1
#     else:
#         return n*a(n-1)
# print(a(5))

# FEBONACCI OF RECURSSION

# def rec(a):
#     if a<=1:
#         return a
#     else:
#         return (rec(a-1)+rec(a-2))
# a=10
# for i in range(a):
#     print(rec(i))

# SUM OF NUMBER OF AN ARRAY

# def rec(a):
#     if len(a)==0:
#         return 0
#     else:
#         return a[0]+rec(a[1:len(a)])
# print(rec([3,5,7]))

# REVERSE OF  STRING

# def rec(a):
#     if len(a)==0:
#         return ''
#     else:
#         return a[len(a)-1]+rec(a[0:len(a)-1])
# print(rec('abcd'))

# POWER OF X

# def rec(x,n):
#     if n==0:
#         return 1
#     else:
#         return x*rec(x,n-1)
# print(rec(9,3))


# def rec(x):
#     if x[0]=='deep':
#         return ''
#     else:
#         return x[0]+' '+rec(x[1:len(x)])
# print(rec(['gudia','sanu','shristi','suku','deep','puja']))



# arr=[]
# def rec(a,arr):
#     if a<=1:
#         arr.append(a)
#     else:
#         arr.append(a[0])
#         return (rec(a-1)+rec(a-2))
# rec(5,[])
# print(arr)

# a=[5,4,8,7,3]
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]>a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)

# BUBBLE SORT BY USING RECURSSION

# arr=[2,5,3,7,6]
# n=len(arr)
# def rec(arr,n):
   
#     for i in range(0,n-1):
#         if arr[i]>arr[i+1]:
#             arr[i],arr[i+1]=arr[i+1],arr[i]
#     if n>0:
#         rec(arr,n-1)
# rec(arr,n)
# print(arr)

# OR 
# a=[5,4,3,6,7,3]
# n=len(a)
# def rec(a,n):
#     if len(a)==0:
#         return 
#     else:
#         for i in range(0,n-1):
#             if a[i]>a[i+1]:
#                 a[i],a[i+1]=a[i+1],a[i]
#         return rec(a,n-1)
# rec(a,n)
# print(a)

# import math
# a=math.gcd(*A)

# CONTINUOUS SUBARRAY USING RECURSION

# a=[1,2,3]
# def rec(a,s,e):
#     if len(a)==e:
#         return
#     elif s>e:
#         rec(a,0,e+1)
#     else:
#         print(a[s:e+1])
#         rec(a,s+1,e)
# rec(a,0,0)

# SELECTION SORT USING RECURSSION

# a=[3,5,2,6,7]
# result=[]
# def rec(a,result):
#     if len(a)==0:
#         return
#     else:
#         j=a.index(min(a))
#         a[0],a[j]=a[j],a[0]
#         result.append(a[0])
#         return rec(a[1:],result)
# rec(a,result)
# print(result)

# quote='The broken fox jumps over the lazy dog'
# new=''
# quote1=quote.lower()
# for i in range(len(quote1)):
#     if quote1[i]==' ':
#         new=new+quote1[i+1].upper()
#     else:
#         new=new+quote1[i]
# print(new)


# OR 

# quote='The broken fox jumps over the lazy dog'
# new=''
# quote_small=quote.lower()
# quote1=quote_small.split()
# new=new+quote1[0]
# for i in range(1,len(quote1)):
#     a=quote1[i].capitalize()
#     new=new+a
# print(new)

# BINARY SEARCH

# def binary(arr,start,end,number):
#     if start<=end:
#         mid=start+(end-start)//2 #6
#         if arr[mid]==number:
#             return mid
#         elif arr[mid]>number:
#             return binary(arr,start,mid-1,number)
#         elif arr[mid]<number:
#             return binary(arr,mid+1,end,number)
#     else:
#         print('not in empty')
# arr=[1,2,3,4,5,6,7,8,9,10]
# number=4
# print(binary(arr,0,len(arr)-1,number))


# MERGE SORT
 

def mergeSort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        mergeSort(left)
        mergeSort(right)
        left_index=0
        right_index=0
        position=0
        while left_index<len(left) and right_index<len(right):
            if left[left_index]<right[right_index]:
                arr[position]=left[left_index]
                left_index+=1
            else:
                arr[position]=right[right_index]
                right_index+=1
            position+=1
        while left_index<len(left):
            arr[position]=left[left_index]
            position+=1
            left_index+=1
        while right_index<len(right):
            arr[position]=right[right_index]
            position+=1
            right_index+=1
arr=[31,5,6,4,1,3,9,11,2,7]
mergeSort(arr)
print(arr)

