# # Factorial Number
# def recursion(a):
#     if a==1:
#         return 1
#     else:
#         return a*recursion(a-1)                                    
# print(recursion(5))




# # fibonacci series
# def fib(n):
#     if n==0:
#         # arr.append(0)
#         return 0
#     elif n==1:
#         # arr.append(1)
#         return 1
#     else:
        
#         # return fib(n-1,arr)+fib(n-2,arr)
#         # return fib(n-1,arr)+fib(n-2,arr)
#         # return arr.append(fib(n-1,arr)+fib(n-2,arr))

#         return fib(n-1)+fib(n-2)
# # arr=[]
# # fib(10,arr)
# # print(arr)
# print(fib(5))


# def fib(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# for i in range(1,5):
#     print(fib(i))
        



# # sum of number an array
# a=[1,2,3,4,5]
# def recursion(a):
#     if len(a)==0:
#         return 0
#     else:
#         return a[0]+recursion(a[1:len(a)])
# print(recursion(a))




# # Reverse
# a="abcde"
# def recursion(a):
#     if (len(a))==0:
#         return " "
#     else:
#         return a[(len(a)-1)] + recursion(a[0:len(a)-1])
# print(recursion(a))




# # power
# def recursion(x,n):
#     if n==0:
#         return 1
#     else:
#         return (x*recursion(x,n-1))
# print(recursion(2,5))




# # reverse before string
# name = ["Swarnalata","Soudamini","Gulnaaz","Trupti"]
# def recursion(name):
#     if name[0]=="target":
#         return name[0]
#     else:
#         return recursion(name[1:len(name)])
# print(recursion(name))


# arr=["a","b","c","d","e","f","g","h","i"]
# result=[]
# def fun1(arr,result):
#     if arr[0]=="f":
#         return " "
#     else:
#         result.append(arr[0])
#         return fun1(arr[1:],result)
# print(fun1(arr,result))
# print(result)
    



# # Bubble Sort
# arr=[5,4,2,1,3]
# n=5
# def rec(arr,n):
#     for i in range(0,n-1):
#         if arr[i]>arr[i+1]:
#             arr[i],arr[i+1]=arr[i+1],arr[i]
#     if n>0:
#         rec(arr,n-1)
# rec(arr,n)
# print(arr)




# # Sub Array
# arr=[1,2,3]
# def rec(arr,start,end):
#     if len(arr)==end:
#         return 
#     elif start>end:
#         return rec(arr,0,end+1)
#     else:
#         print(arr[start:end+1])
#         return rec(arr,start+1,end)
# # arr=[1,2,3]
# print (rec(arr,0,0))