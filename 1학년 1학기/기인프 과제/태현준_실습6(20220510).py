# 4반 4조 20221627 태현준 실습6


print("*****문제1*****")

menu = {"그린티라떼" : 3000, "모카라떼" : 3500, "아메리카노" : 2000, "카페라떼" : 2500} # 메뉴 사전 개체 형성

print("*메뉴 가격 찾기입니다") # 안내문구 출력

choice = "aaaaa" # 아래 반복문에서 input값 저장할 변수 만들어두기.

while True : # True인 동안 반복.
    choice = input("메뉴? ") # 메뉴 입력

    if choice == "" : # 만약 입력한 메뉴가 빈 문자열이면,
        break # 반복문을 종료
    elif choice in menu : # 만약 입력한 메뉴가 메뉴 사전개체 안에 있으면
        print("{} {}원".format(choice, menu[choice])) # 메뉴 이름 키값과 가격 밸류값 출력
    elif choice not in menu : # 만약 입력한 메뉴가 빈 문자열이 아니고 사전개체 안에 없으면
        print("없는 메뉴!") # 없는 메뉴! 출력



print("*****문제2*****")


f = open("C:/Users/user/OneDrive/바탕 화면/Python/기인프 과제/data.txt", "r") # 파일 열기
a = f.read() # a에 f.read하기
print("**읽은 문자열") # **읽은 문자열 출력
print(a) # a 출력

b = "~!@#$%^&*-_+=(){}[]:;?.,<>" # 검사할 특수문자들
c = [] #공백 리스트 형성
d = "" #공백 문자열 형성
for i in range (len(a)) : # 문자열 a의 길이만큼 반복
    if a[i] not in b : # a 안에 문자 하나하나씩 b 안에 있나 없나 검사
        c.append(a[i]) # b 안에 없으면 그 문자를 리스트 c에 추가
    else : # b안에 있으면, 즉 특수문자면
        c.append(" ") # 특수문자 대신 공백 넣기

for i in c : # c의 요소 개수만큼
    d = d + i # 문자열 d에 추가. 문자열 d는 특수문자들 제거한 상태.

print("**새 문자열") # **새 문자열 출력
print(d) # d 출력

c = d.split(" ") # 리스트 c에 문자열 d를 split 해서 넣음.

while "" in c : # 리스트 c 안에 빈칸 개체가 있는 경우
    c.remove("") # c.remove로 없애주기


e = {} # 빈 사전 형성

for i in c : #리스트 요소 개수만큼 반복. 리스트 단어 그대로 i에 넣어줌.
    if i != " " and i in e : # 그 단어가 빈칸이 아니고 사전 안에 있으면
        e[i] = e[i] + 1 # 그 키값에 해당하는 밸류값 1 높이기
    elif i != " " and i not in e : # 그 단어가 빈칸이 아니고 사전 안에 없으면
        e[i] = 1 # 밸류값 1로 해서 추가하기
        

for i, k in e.items() : # 사전개체 요소 개수만큼 반복. 키값 밸류값 둘 다 i k에 넣기
    print("{:10}{:2}".format(i, k)) # 하나씩 출력. 키값은 10자리, 


f.close() # 파일 닫기