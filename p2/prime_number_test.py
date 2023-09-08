inp=int(input())
count=0
for i in range(1,inp+1):
    if inp%i==0:
        count+=1
    i+=1

if count>2:
    print('not prime')
elif count==2:
    print('prime')
else:
    print('error')