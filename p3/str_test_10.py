
def irsa(dinp):
    lprice=list()
    lscore=list()
    irsa=False
    for i in range(0,dinp):
        price , score = input().split()
        lprice.append(price)
        lscore.append(score)
    
    for i in range (0,dinp):
        if lscore[i]>lprice[i] and lscore[i]>lscore[i-1]:
            irsa=True
    return irsa


inp=int(input())
happy_irsa=irsa(inp)
if happy_irsa:
    print('happy irsa')
else:
    print('poor irsa')