L=[4,2,'a',20,44,55]
for ind in range(0,len(L)//2):
    L[ind],L[-ind-1]=L[-ind-1],L[ind]
print(L)