def findword(inp):
    strab=False
    inp=inp.upper()
    if 'AB' in inp:
        inp=inp.replace("AB","",1)
        strab=True
    print(inp)
    if 'BA'in inp and strab==True:
        return (True)
    else:
        return(False)

inp=input()
if findword(inp):
    print('YES')
else:
    print('NO')