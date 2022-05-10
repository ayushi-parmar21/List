a=[2,67,4,6,4,6,4,45,12]
i=0
min1=a[i]
min2=a[i]
while i<len(a):
    if a[i]<min1:
        min1=a[i]
    i+=1
while i<len(a):
    if a[i]>min1:
        if a[i]<min2:
            min2=a[i]
    i+=1
print(min1)
print(min2)