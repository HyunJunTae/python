
num = int(input("정수 개수 : "))

list = input("").split()

big = 0
small = 1000000000000

for i in range (num) :
    if big < int(list[i]) :
        big = int(list[i])
    if small > int(list[i]) :
        small = int(list[i])

print("{} {}".format(small, big))   