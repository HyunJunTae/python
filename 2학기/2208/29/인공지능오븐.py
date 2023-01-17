a, b, c = map(int, input().split())
d = int(input())

d = d % 86400

a += int(d/3600)
b += int(d%3600/60)
c += d%3600%60

if (c >= 60) :
    c -= 60
    b += 1
if (b >= 60) :
    b -= 60
    a += 1
if (a >= 24) :
    a -= 24
    
print(a, b, c)



# #1
# h, m, s = map(int, input().split())
# t = int(input())

# s += t

# m += s // 60
# s = s % 60

# h += m // 60
# m = m % 60

# h = h % 24
    
# print(h, m, s, end='')


# #2
# h,m,s=map(int,input().split())
# s+=int(input())
# m+=s//60
# h+=m//60
# print(h%24,m%60,s%60)