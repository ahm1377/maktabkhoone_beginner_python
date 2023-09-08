def prog():
    countmax=0
    inpmax=0
    inp=1
    for i in range(0,20):
        inp=int(input())
        count=0
        j=1
        while j<=inp:
            if int(inp) %j==0:
                count+=1
            j+=1
        if count>countmax:
            countmax=count
            inpmax=inp
        elif count==countmax:
            if inp>inpmax:
                inpmax=inp
    
    
    print(inpmax ,'    ',countmax)


prog()