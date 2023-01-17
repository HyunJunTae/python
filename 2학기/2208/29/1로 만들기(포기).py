n = int(input("n : "))

count = 0
while(n != 1) :
    if (n%3 == 0) :
        n /= 3
    elif (n%2 == 0 and (n-1)%3 != 0) :
        n /= 2
    else :
        n -= 1
    count += 1
print(count)



# 123
# 1 3 9 27 81 
# 1 3 9 27 54 108



# 123 122 61 60 20 10 5 4 2 1
# 123 122 121 120 40 20 10 5 4 2 1