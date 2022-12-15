n=[1,2,3,4,5]
sub_arry=[]
sum=0
for i in range(0,len(n)):
    for j in range(i,len(n)):
        sub_arry.append(n[i:j])
        sum=sum+sub_arry[i][j]
        if sum % 3 !=0:
            print(sum)
        # print(sub_arry)
        