from collections import OrderedDict

def dictionary(lineNumber):
    ara=OrderedDict()
    for i in range(0,lineNumber):
        raye=input()
        if raye in ara:
            ara[raye]+=1
        else:
            ara[raye]=1
    return ara

line_number=int(input())
arac=dictionary(line_number)
arackey=list(arac.keys())
arackey.sort()
for i in arackey:
    print(i,arac[i])