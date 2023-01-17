n = int(input())
num = input()
sum = 0
# for i in range(n) :
    # sum += int(num[i])
    # 이렇게 하면 왜 런타임에러??
    
for i in num :
    sum += int(i)

print(sum)