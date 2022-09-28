n = int(input())
bin = []

for i in range(n) :
    num = int(input())
    
    while(num != 0) :
        a = num%2
        bin.append(a)
        
        num //= 2
        # 파이썬에서 / 하면 나누기. 1/2 하면 0.5가 됨. // 해야 몫.
    
    for j in range(len(bin)) :
        if (bin[j] == 1) :
            print(j, end=' ')
    
    bin = []