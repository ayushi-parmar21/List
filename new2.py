a=[7,2,[3,4,[5,6]],7,8]
for i in a:
    if type(i)==list:
        for j in i:
            if type(j)==list:
                for k in j:
                    print(k)
            else:
                print(j)
    else:
        print(i)