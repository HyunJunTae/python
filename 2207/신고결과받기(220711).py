
# def print_coin() :
#     print("비트코인")
    
    
    
    
# print_coin()


# for i in range(100) :
#     print_coin()
    
    
# def print_coins() :
#     for i in range(100) :
#         print_coin()




# a = 3
# b = 5
# num_list = []
# sum = 0

# while(a < 1000) :
#     if a not in num_list :
#         num_list.append(a)
#     a = a + 3

# while(b < 1000) :
#     if b not in num_list :
#         num_list.append(b)
#     b = b + 5

# for i in num_list :
#     sum = sum + i
    
# print(sum)




                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
#### 신고 결과 받기                 
                    

## 기본 정보
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2


## 신고 몇 번 당했는지 계산.
result = [0 for i in range(0, len(id_list))]
report_add = []
for i in report :
    if (i in report_add) : # 만약 a사람이 b사람이 신고 이미 신고된 리스트에 잇으면
        continue # 그건 계산 안하고 넘기기
    a, b = i.split()
    for j in range(len(id_list)) : # 신고 받은 사람 이름인
        if (id_list[j] == b) : # id_list에서 몇 번째에 있는지 찾아내서
            result[j] = result[j] + 1 # result 리스트에 추가해주기
    report_add.append(i)


## 정지인지 아닌지 판별하고 정지면 stop 리스트에 추가
stop = []
for i in range(len(result)) :
    if (result[i] >= k) :
        stop.append(id_list[i])



## 정지이면 그 사람 신고한 사람들한테 메일 보내주기
mail = [0 for i in range(0, len(id_list))]

for i in report :
    a, b = i.split()
    if b in stop :
        mail[id_list.index(a)] = mail[id_list.index(a)] + 1
print(mail)