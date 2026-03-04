l=[5,1,3,4,2,6,7,0]
target=7
for ind1 in range(0,len(l)-1):
    for ind2 in range(ind1+1,len(l)):
        if l[ind1]+l[ind2]==target:
            print(l[ind1],l[ind2])