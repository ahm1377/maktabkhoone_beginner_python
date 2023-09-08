def hello(definp):
    inplen=len(definp)
    count=0
    countword=0
    hello=''
    while count<inplen:
        if countword==0 and definp[count]=='h':
            countword += 1
            hello=hello+'h'
        if countword==1 and definp[count]=='e':
            countword += 1
            hello=hello+'e'
        if countword==2 and definp[count]=='l':
            countword += 1
            hello=hello+'l'
        if countword==3 and definp[count]=='l':
            countword += 1
            hello=hello+'l'
        if countword==4 and definp[count]=='o':
            countword += 1
            hello=hello+'o'
        count+=1
    if countword==5 and hello=='hello':
        return('YES')
    else:
        return('NO')

inp=input().lower()
print(hello(inp))