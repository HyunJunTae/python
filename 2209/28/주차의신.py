n = int(input())

for i in range(n) :
    num = int(input())
    park = list(map(int, input().split()))
    print(2*(max(park)-min(park)))
    park = []