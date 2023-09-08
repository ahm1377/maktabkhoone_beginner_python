import random 
a=0
b=100
rand=0
ans=' '
while ans!='d':
    rand=random.randint(a,b)
    print(rand , '?=')
    ans=input()
    if ans=='k':
        b=rand+1
    elif ans=="b":
        a=rand+1
    elif ans=="d":
        print('you win')
        break
    else:
        print('!!!error!!!')
             