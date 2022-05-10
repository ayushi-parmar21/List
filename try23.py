list1=[2,3,[4],5,6,[7,8]]
list2=[]
i=0
while i<len(list1):
    if type(list1[i])==list:
        j=0
        while j<len(list1[i]):
            list2.append(list1[i][j])
            j+=1
    else:
        list2.append(list1[i])
    i+=1
j=0
while j<len(list2):
    sum=0
    k=-1
    while k>-len(list2):
        sum=list2[j]+list2[k]
        k-=1
    print(sum)
    j+=1
