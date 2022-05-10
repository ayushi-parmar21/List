lst=["a","bc","abc","de","xyz"]
i=0
max=0
list=[]
mul=1
while i<len(lst):
    count=0
    j=0
    while j<len(lst[i]):
        count+=1
        if count>max:
            max=count
        j+=1
    list.append(count)
    i+=1 
print(max)
for k in list:
    if max==list[k]:
        mul=mul*list[k]
print(mul)
    