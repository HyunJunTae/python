#### 신고 결과 받기                 
                    

## 기본 정보
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2


# ## 신고 몇 번 당했는지 계산.
# result = [0 for i in range(0, len(id_list))] # 원소가 모두 0인 리스트. id_list의 길이만큼 원소 개수 생성.
# report_add = []
# for i in report :
#     if (i in report_add) : # 만약 a사람이 b사람이 신고 이미 신고된 리스트에 잇으면
#         continue # 그건 계산 안하고 넘기기
#     a, b = i.split()
#     for j in range(len(id_list)) : # 신고 받은 사람 이름인
#         if (id_list[j] == b) : # id_list에서 몇 번째에 있는지 찾아내서
#             result[j] = result[j] + 1 # result 리스트에 추가해주기
#     report_add.append(i)


# ## 정지인지 아닌지 판별하고 정지면 stop 리스트에 추가
# stop = []
# for i in range(len(result)) :
#     if (result[i] >= k) :
#         stop.append(id_list[i])



# ## 정지이면 그 사람 신고한 사람들한테 메일 보내주기
# mail = [0 for i in range(0, len(id_list))]

# for i in report :
#     a, b = i.split()
#     if b in stop :
#         mail[id_list.index(a)] = mail[id_list.index(a)] + 1
# print(mail)










#### 신고 결과 받기                 
       
def solution(id_list, report, k) :
    ## 신고 몇 번 당했는지 계산.
    result = [0 for i in range(0, len(id_list))] # 원소가 모두 0인 리스트. id_list의 길이만큼 원소 개수 생성.
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
    
    return mail

            






#### 신고 결과 받기                 
       
def solution1(id_list, report, k) :
    report = set(report) ####################################################### 같은 원소를 없앤다. 시간이 단축된다.
    ## 신고 몇 번 당했는지 계산.
    result = [0 for i in range(0, len(id_list))] # 원소가 모두 0인 리스트. id_list의 길이만큼 원소 개수 생성.
    for i in report :
        a, b = i.split()
        for j in range(len(id_list)) : # 신고 받은 사람 이름인
            if (id_list[j] == b) : # id_list에서 몇 번째에 있는지 찾아내서
                    result[j] = result[j] + 1 # result 리스트에 추가해주기


    ## 정지인지 아닌지 판별하고 정지면 메일 보내주기
    mail = [0] * len(id_list)
    for i in range(len(result)) :
        if (result[i] >= k) :
            for j in report :
                a, b = j.split()
                if (b == id_list[i]) :
                    mail[id_list.index(a)] = mail[id_list.index(a)] + 1
            
    return mail







# #### 신고 결과 받기                 
       
# def solution2(id_list, report, k) :
#     report = set(report) ####################################################### 같은 원소를 없앤다. 시간이 단축된다.
    
#     # 신고 횟수 저장할 딕셔너리 만들기
#     report_do = {}
#     for i in id_list :
#         report_do[i] = 0
#     report_be = {}
#     for i in id_list :
#         report_be[i] = 0
#     # 딕셔너리에 신고 횟수 저장
#     for i in report :
#         a, b = i.split()
#         report_do[a] += 1
#         report_be[b] += 1
    
#     # ## 딕셔너리의 value값을 리스트로 하여 신고 한 횟수 신고 당한 횟수 한 번에 할 수 없나?
#     # report_ex = {}
#     # for i in id_list :
#     #     report_ex = [0,0]
    
#     # for i in report :
#     #     report_ex
    
    
    
#     # 정지인지 아닌지 판별하고 정지면 메일 보내주기
#     mail = [0] * len(id_list)
#     for i, j in report_be.items() :
                
#     return mail

             




print(solution(id_list, report, k))