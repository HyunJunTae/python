# 20221627 태현준 실숩

print("*****문제1*****") #문제1 표시

medals= [['Austria',0,2,1], ['Canada',4,8,5], ['China',5,0,1],['France',0,4,5], ['Germany',1,1,2], ['Japan',1,1,0], ['Korea',5,3,1], ['Norway',4,4,7], ['Russia',4,6,4], ['Viet Nam',1,1,5] ]
#리스트 형성

for i in range (len(medals)) : #medals 리스트의 요소 개수만큼 반복
    a = medals[i][1] + medals[i][2] + medals[i][3] #메달 3개 더해서 a에 저장
    medals[i].append(a) #a를 append


for i in range (len(medals)) : #medals 리스트의 요소 개수만큼 반복
    print(medals[i]) #메달 한 나라씩 출력
    
print("\n") #한 줄 띄우기
    
print(medals) #메달 리스트 전체 출력


## 이 주석은 개인적으로 공부하려고 달아둔거라서 무시해주세요..!
# 맨 처음에 파이썬 까먹어서 for i in range medals 했음 당연히 안됨 
# 다음엔 for i in medals 했음 이러면 되긴 되는데 medals에 값 하나하나가 i에 들어가는거니까
# 다음 줄에서 i번째 머시기머시기 할 때 안됨
# 그래서 for i in range (len(medals))로 해아함



print("*****문제2*****") # 문제 2 표시

a = input("입력하세요\n") # 문자열 입력 
b = "~!@#$%^&*-_+=(){}[]:;?.,<>" # 검사할 특수문자들
c = [] #공백 리스트 형성
d = "" #공백 문자열 형성
for i in range (len(a)) : # 문자열 a의 길이만큼 반복
    if a[i] not in b : # a 안에 문자 하나하나씩 b 안에 있나 없나 검사
        c.append(a[i]) # b 안에 없으면 그 문자를 리스트 c에 추가

for i in c : # c의 요소 개수만큼
    d = d + i # 문자열 d에 추가. 문자열 d는 특수문자들 제거한 상태.

c = d.split(" ") # 리스트 c에 문자열 d를 split 해서 넣음.

print(d)

e = {} # 빈 사전 형성

for i in c : #리스트 요소 개수만큼 반복. 리스트 단어 그대로 i에 넣어줌.
    if i in e : # 그 단어가 사전 안에 있으면
        e[i] = e[i] + 1 # 그 키값에 해당하는 밸류값 1 높이기
    else : # 없으면
        e[i] = 1 # 밸류값 1로 해서 추가하기
        

for i, k in e.items() : # 사전개체 요소 개수만큼 반복. 키값 밸류값 둘 다 i k에 넣기
    print("{:10}{:2}".format(i, k)) # 하나씩 출력. 키값은 10자리, 