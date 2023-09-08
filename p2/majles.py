inp=0
max_avg=0
while inp != -1:
    inp=int(input())
    if inp>10 and inp<90:
        if inp>max_avg:
            max_avg=inp
    
print(max_avg)