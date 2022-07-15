# a = list(range(1,10001))
# b = list(range(1,10001))


# for i in a :
#     c = str(i)
#     for j in c :
#         i = i + int(j)
#     if i <= 10000 :
#         b.remove(i)
        
# print(b)

# 아 ㅋㅋㅋㅋㅋ; b.remove(i)에서 오류나는게, 리스트에 이미 없는 값 뺄려고 하면 오류나는거.
# 101은 91로도 만들수있고 100으로도 만들 수 있다. ㅋㅋㅋㅋㅋ 아 맙소사네
# 1에서 10000까지 가득 찬 리스트에서 빼는 방식으로는 너무 복잡함.






a = list(range(1,10001))
b = []

for i in a :
    c = str(i)
    for j in c :
        i = i + int(j)
    if i <= 10000 and i not in b:
        b.append(i)
      
for i in b :
    a.remove(i)

print(a)
# 와 리스트끼리는 빼는게 안되네 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ a - b가 안되네
# 반복문으로 빼볼라했는데 왜 자꾸 remove 오류가뜨지~~~~~~ print(b) 해보면 10000 안되는데 다들 아 설마 겹치는 숫자가 있나
# 아 맞네 겹치는게 있었네 b 안에 i not in b 추가하니까 바로 되네 얏호우


# 오늘의 교훈. 리스트에 없는 값을 빼려고 하면 오류가 난다~
# 너무 한 가지 방법에 사로잡히지 말자.




# set로 차집합 써서 하는것도 있길래 해봄

# a = set(range(1,10001))
# b = set()
# # b = {} 하면 빈 사전개체 생성됨.

# for i in a :
#     c = str(i)
#     for j in c :
#         i = i + int(j)
#     if i <= 10000 :
#         b.add(i)
        
# c = a - b
# for i in c :
#     print(i)
# 이러면 순서가 뒤죽박죽이야 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ 아 무치겠다.