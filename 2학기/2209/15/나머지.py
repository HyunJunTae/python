l = []
count = 0
for i in range(10) :
    a = int(input())
    a %= 42
    if (a in l) :
        continue
    l.append(a)
    count += 1
print(count)