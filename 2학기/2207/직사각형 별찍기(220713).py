
# # 이거는 그냥 개쉽게 한거
# n, m = input().split()

# for i in range(int(m)) :
#     for j in range(int(n)) :
#         print("*", end="")
#     print("")




# map, strip 사용.

a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b
print(answer)

# map으로 int형으로 바꿔주는 것.
# input으로 받으면 문자형이니까 map으로 int로 바꿔줌.
# strip으로 공백을 지워줌. 선행, 후행하는 공백.
#                          5 3                                          이렇게 입력을 해도 작동을 하는거지.