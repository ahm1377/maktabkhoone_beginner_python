inp=input()

def inp_upper_lower(inp):
    lowinp=''
    inplen=0
    lowword=0
    uppword=0

    inplen=len(inp)
    lowinp=inp.lower()
    for i in range(0,inplen):
        if inp[i]==lowinp[i]:
            lowword+=1
        else:
            uppword+=1
    if lowword>=uppword:
        return (inp.lower())
    else:
        return (inp.upper())

print(inp_upper_lower(inp))