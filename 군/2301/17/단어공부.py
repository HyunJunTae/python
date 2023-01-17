alpha = input().upper()

## 대문자로 바꾸기 - upper 사용. 입력받을 때부터 바로 사용 가능.
# alpha2 = ""

# for i in range (0, len(alpha)) :
#     if (97 <= ord(alpha[i])) :
#         alpha2 += chr(ord(alpha[i])-32)
#         continue
#     alpha2 += alpha[i]

alpha_dict = {}
for i in alpha :
    if (i in alpha_dict) :
        alpha_dict[i] += 1
        continue
    alpha_dict[i] = 1

keys = list(alpha_dict.keys())
values = list(alpha_dict.values())
m = max(values)
ind = values.index(m)
values.remove(m)

if (m == max(values)) :
    print("?")
else :
    print(keys[ind])