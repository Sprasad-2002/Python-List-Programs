count=0
for num in range(1,101):
    if num>1:
        for val in range(2,int(num**0.5)+1):
            if num %val==0:
                break
        else:
            count+=1
            if count%2==1:
                print(num)
                
                