print("20221627 태현준 과제 4")
print() #한 줄 띄우기

print("***** 문제 1 *****")

a = int(input("경과 일을 입력하세요 : ")) #경과일 입력
today = "" #판별 값 넣을 변수 만들어두기
#오늘은 화요일

#경과일 7로 나누기
if a % 7 == 0 :  #7로 나눠서 0이면
    today = "화" #화요일
if a % 7 == 1 :  #7로 나눠서 1이면
    today = "수" #수요일
if a % 7 == 2 :  #7로 나눠서 2이면
    today = "목" #목요일
if a % 7 == 3 :  #7로 나눠서 3이면
    today = "금" #금요일
if a % 7 == 4 :  #7로 나눠서 4이면
    today = "토" #토요일
if a % 7 == 5 :  #7로 나눠서 5이면
    today = "일" #일요일
if a % 7 == 6 :  #7로 나눠서 6이면
    today = "월" #월요일

print("{}일 후는 {}요일".format(a, today)) #문자열 포맷팅으로 출력
print() #한 줄 띄우기

print("***** 문제 2 *****")

a = int(input("경과 일을 입력하세요 : ")) #경과일 입력
days = "화수목금토일월" #요일 문자열 구성
days = days[a % 7] #경과일 7로 나눠서 0이면 days[0] = 화. 1이면 수 등으로 됨.

print("{}일 후는 {}요일".format(a, days)) #문자열 포맷팅으로 출력
print() #한 줄 띄우기

print("***** 문제 3 *****")

#메달 리스트 만들기
medals= [ ['Austria',0,2,1], ['Canada',4,8,5], ['China',5,0,1],
['France',0,4,5], [ 'Germany',1,1,2], ['Japan',1,1,0],
['Korea',5,3,1], ['Norway',4,4,7], ['Russia',4,6,4],
['Viet Nam',1,1,5] ]

medals[0].append(3) #medals 리스트의 0번 내부리스트에 메달 개수 합 append
medals[1].append(17) #medals 리스트의 1번 내부리스트에 메달 개수 합 append
medals[2].append(6) #medals 리스트의 2번 내부리스트에 메달 개수 합 append
medals[3].append(9) #medals 리스트의 3번 내부리스트에 메달 개수 합 append
medals[4].append(4) #medals 리스트의 4번 내부리스트에 메달 개수 합 append
medals[5].append(2) #medals 리스트의 5번 내부리스트에 메달 개수 합 append
medals[6].append(9) #medals 리스트의 6번 내부리스트에 메달 개수 합 append
medals[7].append(15) #medals 리스트의 7번 내부리스트에 메달 개수 합 append
medals[8].append(14) #medals 리스트의 8번 내부리스트에 메달 개수 합 append
medals[9].append(7) #medals 리스트의 9번 내부리스트에 메달 개수 합 append

print(medals[0]) #medals 리스트의 0번 내부리스트 출력
print(medals[1]) #medals 리스트의 1번 내부리스트 출력
print(medals[2]) #medals 리스트의 2번 내부리스트 출력
print(medals[3]) #medals 리스트의 3번 내부리스트 출력
print(medals[4]) #medals 리스트의 4번 내부리스트 출력
print(medals[5]) #medals 리스트의 5번 내부리스트 출력
print(medals[6]) #medals 리스트의 6번 내부리스트 출력
print(medals[7]) #medals 리스트의 7번 내부리스트 출력
print(medals[8]) #medals 리스트의 8번 내부리스트 출력
print(medals[9]) #medals 리스트의 9번 내부리스트 출력
print() #한 줄 띄우기

print(medals) #medals 리스트 출력


