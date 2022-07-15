# 20221627 태현준 실숩

print("*****문제1*****") #문제1 표시

medals= [['Austria',0,2,1], ['Canada',4,8,5], ['China',5,0,1],['France',0,4,5], ['Germany',1,1,2], ['Japan',1,1,0],['Korea',5,3,1], ['Norway',4,4,7], ['Russia',4,6,4], ['Viet Nam',1,1,5] ]
#리스트 형성

for i in range (len(medals)) : #medals 리스트의 요소 개수만큼 반복
    a = medals[i][1] + medals[i][2] + medals[i][3] #메달 3개 더해서 a에 저장
    medals[i].append(a) #a를 append


for i in range (len(medals)) : #medals 리스트의 요소 개수만큼 반복
    print(medals[i]) #메달 한 나라씩 출력
    
print("\n") #한 줄 띄우기
    
print(medals) #메달 리스트 전체 출력


# 맨 처음에 파이썬 까먹어서 for i in range medals 했음 당연히 안됨 
# 다음엔 for i in medals 했음 이러면 되긴 되는데 medals에 값 하나하나가 i에 들어가는거니까
# 다음 줄에서 i번째 머시기머시기 할 때 안됨
# 그래서 for i in range (len(medals))로 해아함


print("*****문제2*****") # 문제 2 표시

menu = {"쥬스" : 4000, "모카라떼" : 3500, "아메리카노" : 2000, "카페라떼" : 3000} # 메뉴 사전개체 형성

print("* 모든 메뉴:") # * 모든 메뉴: 출력

for i in menu.keys() : # 사전 개체 요소 개수만큼 반복. len를 이용해서 0, 1, 2를 i에 넣는게 아니라 사전개체 키값 자체를 넣음.
    print(i, end = " ") # 키값인 메뉴 이름들 출력. end=" "로 줄 안바뀌고 띄어쓰기로 이어지도록 함.

print("\n") # 한 줄 띄우기


print("* 메뉴별 가격:") # * 메뉴별 가격: 출력
    
for i, k in menu.items() : # 사전 개체 요소 개수만큼 반복. 사전개체의 키값과 밸류값을 i, k에 넣음.
    print("{} {}원".format(i, k)) # 키값인 메뉴 이름과 밸류값인 가격 출력. 