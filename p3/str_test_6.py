def palindrome(inp):
    inplen2=int(len(inp)/2)
    paznum=0
    negnum=-1
    for i in range(0,inplen2):
        if inp[paznum]==inp[negnum]:
            paznum+=1
            negnum-=1
    if paznum==inplen2:
        return (True)
    else:
        return (False)
    

inp=(input().lower())
if palindrome(inp):
    print('palindrome')
else:
    print('not palindrome')