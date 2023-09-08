def pointlen(pointlist):
    pointlist.sort()
    fasele12=abs(float(pointlist[0])-float(pointlist[1]))
    fasele13=abs(float(pointlist[0])-float(pointlist[2]))
    fasele23=abs(float(pointlist[1])-float(pointlist[2]))
    sumwalk=min(fasele12 + fasele13, fasele13 + fasele23, fasele12 + fasele23)
    if sumwalk%1==0.00:
        sumwalk=int(sumwalk)
    return(sumwalk)

inp=input()
point3=inp.split()
print(pointlen(point3))