def if3(definp):    
    chek=''
    for char in definp:
        char=char.lower()
        if char != 'a' and char != 'o'and char != 'u'and char != 'i'and char != 'e':
            chek= chek + '.' + char
    return(chek)

inp=input()
print(if3(inp)) 