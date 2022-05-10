a=[7,2,[5.2,3],8.2,0.2,"ayu"]
sum=0
for i in a:
    if type(i)==list:
        for j in i:
            if type(j)==float:
                sum+=j
    else:
        if type(i)==float:
            sum+=i
print(sum)  