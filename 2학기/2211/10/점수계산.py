# a = []
# for i in range(8) :
#     a.append(int(input()))

# b = []
# sum = 0
# for i in range(5) :
#     k = a.index(max(a))
#     sum += a[k]
#     b.append(k)
#     a[k] = 0

# b.sort()

# print(sum)
# for i in range(5) :
#     print(b[i]+1, end = ' ')




# score_dic = {}
# sum = 0

# for i in range(8) :
#     sc = int(input())
#     sum += sc
#     score_dic[sc] = i
    
# score_sorted = list(sorted(score_dic.items())) # sorted 하면 리스트 반환됨.

# print(sum)
# print(score_sorted)
# for i in range(3, 8) :
#     print(score_dic[i][1], end=" ")





score_dic = {}

for i in range(8) :
    score_dic[i] = int(input())