a = []

while(1) :
    n = int(input())
    
    if (n == -1) :
        break
    
    for i in range (1, n) :
        if (n%i == 0) :
            a.append(i)
    
    if (sum(a) == n) :
        print("{} = {}".format(n, " + ".join(map(str, a))))
    else :
        print("{} is NOT perfect.".format(n))
    
    a = []