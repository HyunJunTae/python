# t = int(input())

# for i in range(t) :
#     a = input().split()
#     num = float(a[0])
#     for j in a :
#         if (j == '@') :
#             num *= 3
#         elif (j == '%') :
#             num += 5
#         elif (j == '#') :
#             num -= 7
#     print("{:.2f}".format(num))
    
    
# 1
t = int(input())
for _ in range(t):
    s = input().split()
    a = float(s[0])
    for x in s[1:]:
        if x == '@': a *= 3
        elif x == '%': a += 5
        else: a -= 7
    print("%.2f"%a)