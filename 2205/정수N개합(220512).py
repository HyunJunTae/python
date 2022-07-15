## 숫자 n개 입력받아서 리스트 a에 보내고, 함수에서 리스트 계산해서 다 더한 값 return하기.

def add(list, num) :
    result = 0
    for i in range(n) :
        result = result+ list[i]
    
    return result
    
    

a = []
b = 1
n = 0

print("숫자 입력을 종료하려면 0을 입력")
while b != 0 :
    b = int(input("Input : "))
    a.append(b)
    n = n + 1

print("숫자의 합 : {}".format(add(a, n)))