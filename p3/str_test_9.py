def team(lists,number):

    if len(lists)!=number:
        return '!!! error: your input have problem !!!'
    else:
        count=0
        for i in range(0,number):
            lists[i]=int(lists[i])
        while count!=len(lists):
            if lists[count]>2 or lists[count]<0 :
                del lists[count]
            else:
                count+=1
        outp=int(len(lists)/3)
        return outp

            
    

inp=int(input())
inplist=input().split()
print(team(inplist,inp))