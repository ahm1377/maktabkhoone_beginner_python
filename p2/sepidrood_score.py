SumScore=0
win=0
i=0
while i<30:
    score =int(input())
    if score==0 or score==1 or score==3:
        i+=1
        SumScore+=score
        if score==3:
            win+=1

print(SumScore , win)
