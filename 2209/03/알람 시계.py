a, b = map(int, input().split())

b += a*60 - 45
if (b < 0) :
    b += 1440
    
a = b//60
b = b%60
print(a, b)