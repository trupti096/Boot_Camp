arr=[1,2,3,4,5]
def rec(arr,start,end):
    if len(arr)==end:
        return
    elif start>end:
        return rec(arr,0,end+1)
    else:
        print(arr[start:end+1])
        return rec(arr,start+1,end)
print(rec(arr,0,0))
    
    
    
# def rec(arr,start,end):
#     if len(arr)==end:
#         return
#     elif start > end:
#         return rec(arr,0,end+1)
#     else:
#         print (arr[start:end+1])
#         return rec(arr,start+1,end)
# print(rec(arr,0,0))