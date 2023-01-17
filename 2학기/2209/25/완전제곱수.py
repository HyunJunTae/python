n = int(input())
m = int(input())
a = []

i = 1
while(1) :
    if (i*i in range(n, m+1)) :
        a.append(i*i)
    i += 1
    
    if (i*i > m) :
        break

if (sum(a) == 0) :
     print(-1)
else :
    print(sum(a))
    print(a[0])