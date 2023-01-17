# a = []
# for i in range (5):
#     b, c, d, e = map(int, input().split())
#     a.append(b+c+d+e)

# print("{} {}".format(a.index(max(a))+1, max(a)))






# max = 0
# rank = 0

# for i in range(5) :
#     a, b, c, d = map(int, input().split())
#     if (max < a+b+c+d) :
#         max = a+b+c+d
#         rank = i+1
# print(rank, max)







max = 0
rank = 0

for i in range(5) :
    a, b, c, d = map(int, input().split())
    if (max < a+b+c+d) :
        max = a+b+c+d
        rank = i+1
print(rank, max)