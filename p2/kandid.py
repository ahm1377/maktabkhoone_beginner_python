inp=0
max_avg1=0
max_avg2=0
while inp != -1:
    inp=int(input())
    if inp>10 and inp<90:
        if inp>max_avg1:    
            max_avg2=max_avg1
            max_avg1=inp
        elif inp>max_avg2 and inp<max_avg1:
            max_avg2=inp
    
print(max_avg1 , max_avg2)