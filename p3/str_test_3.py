names=list(range(10))
count=10

def inp_upper_lower():
        inp=input()
        inp= inp[:1].upper() + inp[1:].lower()
        return(inp)

for i in range(0,count):
    names[i]=inp_upper_lower()

for i in range(0,count):
     print(names[i])