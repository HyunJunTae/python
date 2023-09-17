count = int(input())
data = []

for i in range(count) :
    num = int(input())
    data.append(num)

data = sorted(data)

for i in data :
    print(i)