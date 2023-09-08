def translate(inp):
    dictunary=dict()
    textlist=list()
    anser=str()
    count=int()
    while count!=inp:
        key , val =input().split()
        dictunary[key]=val
        count+=1
    textlist=input().split()
    for j in range(0,len(textlist)):
        if textlist[j] in list(dictunary.keys()):
            anser=anser+dictunary[textlist[j]]+' '
        else:
            anser=anser+textlist[j]+' '
    return anser

inp=int(input())
print(translate(inp))