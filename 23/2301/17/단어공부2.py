# 다 대문자로 만들기
alpha = input().upper()

# 딕셔너리 만들기. key : 알파벳 / value : 해당 알파벳 개수
alpha_dict = {}
for i in alpha :
    if (i in alpha_dict) :
        alpha_dict[i] += 1
        continue
    alpha_dict[i] = 1

# max값이 두 개 이상이면 ? 출력
values = list(alpha_dict.values())
if (values.count(max(values)) >= 2) :
    print("?")
    

# max값 한 개일 경우 해당 알파벳 출력
else :
    ind = values.index(max(values))
    print(list(alpha_dict.keys())[ind])