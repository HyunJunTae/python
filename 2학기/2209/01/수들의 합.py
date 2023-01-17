s = int(input())
a = 1
count = 0
while(1) :
    if (s < 2*a+1) :
        count += 1
        break
    else :
        s -= a
        a += 1
        count += 1
print(count)