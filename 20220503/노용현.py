import random
money = int(input("로또 얼마치 할까요?"))






# for i in range (int(money/1000)) :  #로또 가격 한 개당 천원이니까 천원으로 나눔. 6000원이면 6000/1000 = 6. 6번.
#     for i in range (6): #여기부턴 니가 한거 그대로
#         print(random.randint(1,46), end = " ")
#     print()


## money 에서 천 원씩 빼서 0원이 되면 반복문 종류
import random
money = int(input("로또 얼마치 할까요?"))

## money 에서 천 원씩 빼서 0원이 되면 반복문 종류
while money != 0 :
    for i in range (6):
        print(random.randint(1,46), end = " ")
    print()
    money = money - 1000