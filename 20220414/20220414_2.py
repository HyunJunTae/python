#팩토리얼
number = int(input("Number : "))
count = 1

for i in range(1, number+1) :
    count = count * i
    
print(count)


#피보나치 0 1 1 2 3 5
number = int(input("number : "))

a = 0
b = 1
for i in number :
    b = a + b
    a = b - a
    
print("Fibonacci[{}] = []".format(number, b))