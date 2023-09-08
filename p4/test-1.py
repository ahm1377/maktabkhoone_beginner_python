import math
def rishe2(inp):
    rishe=list()
    for i in range (0,inp):
        j=str(math.sqrt(float(input())))
        asl , rish = j.split('.')
        if len(rish)==0:
            rish='0000'
        elif len(rish)==1:
            rish=rish+'000'
        elif len(rish)==2:
            rish=rish+'00'
        elif len(rish)==3:
            rish=rish+'0'
        elif len(rish)>4:
            rish=rish[:4]
        rishe.append(asl+'.'+rish)
    return rishe

inp=int(input())
rishe=rishe2(inp)
for k in range(0,inp):
    print(rishe[k])