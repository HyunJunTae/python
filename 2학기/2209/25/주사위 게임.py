a = 100
b = 100

n = int(input())
for i in range(n) :
    num1, num2 = map(int, input().split())
    if (num1 > num2) :
        b -= num1
    elif (num1 < num2) :
        a -= num2
    
print(a)
print(b)