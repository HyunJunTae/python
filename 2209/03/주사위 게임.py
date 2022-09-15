n = int(input())
num = 0
for i in range (n) :
    a, b, c = map(int, sorted(input().split()))
    if (a==b==c) :
        a = 10000 + a*1000
    elif(a!=b!=c) :
        a = c*100
    else :
        a = 1000 + b*100
    if (a > num) :
        num = a
print(num)