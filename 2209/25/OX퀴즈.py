n = int(input())
point = 0
count = 0

for i in range(n) :
    case = input()
    for j in range(len(case)) :
        if (case[j] == 'O') :
            point += 1 + count
            count += 1
        else :
            count = 0
    print(point)
    point = 0
    count = 0