list_a = []
list_b = []

for i in range(3) :
    a, b = map(int, input().split())
    if (a not in list_a) :
        list_a.append(a)
    elif (a in list_a) :
        list_a.remove(a)
    if (b not in list_b) :
        list_b.append(b)
    elif (b in list_b) :
        list_b.remove(b)
print(list_a[0], list_b[0])