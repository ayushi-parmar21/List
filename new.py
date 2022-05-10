a=["ayushi",7.6,8,9.2,"rani",5]
i=0 
sum=0
while i<len(a):
    if type(a[i])==str:
        pass
    else:
        sum+=a[i]
    i+=1
print(sum)