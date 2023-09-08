def countnum(inp):
    cnum_1=0
    cnum_2=0
    cnum_3=0
    for char in inp:
        if char=='1':
            cnum_1+=1
        elif char=='2':
            cnum_2+=1
        elif char=='3':
            cnum_3+=1
    return(cnum_1,cnum_2,cnum_3)
    
def prntnum(cnum1,cnum2,cnum3):
    str_num=''
    for i in range( 0 ,cnum1):
        str_num=str_num + '+1'
    for i in range( 0 ,cnum2):
        str_num=str_num + '+2'
    for i in range( 0 ,cnum3):
        str_num=str_num + '+3'
    return (str_num[1:])

inp=input()

count_num_1=0
count_num_2=0
count_num_3=0
outp=''

count_num_1,count_num_2,count_num_3=countnum(inp)
outp=prntnum(count_num_1,count_num_2,count_num_3)
print(outp)