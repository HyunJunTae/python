sum = 0
i = 0
j = 0

a, b = map(int, input().split())

while(1) :
    i += 1
    if (i >= a) :
        break
    a -= i
    
while(1) :
    j += 1
    if (j >= b) :
        break
    b -= j

if (i == j) :
    sum = sum + (b-a+1)*i
else :
    sum += sum + (i-a+1)*i + b*j
    for k in range(i+1, j) :
        sum = sum + k*k

print(sum)