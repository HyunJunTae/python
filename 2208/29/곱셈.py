a = int(input())
b = int(input())

for i in list(map(int, reversed(str(b)))) :
    print(a * int(i))
print(a*b)