print("20221627 태현준 실습#2")
print()

print("***** 문제1 *****")
근무시간 = int(input("근무시간? ")) #근무시간 입력
급여 = int(input("시간당 급여? ")) #시간당 급여 입력 
원징세 = float(input("원천징수세율? ")) #원천징수세율 입력
주세 = float(input("주민세율? ")) #주민세율


print("="*20) #= 20번 출력
print("*총 급여 : {}원".format(근무시간*급여)) #총 급여 계산
print("*공제 : \n원천징수세 ({}) : {}원".format(원징세, 근무시간*급여*원징세 )) #원천징수세 계산
print("주민세 ({}) : {}원".format(주세, 근무시간*급여*주세 )) #주민세 계산
print("총 공제 : {}원".format(근무시간*급여*원징세 + 근무시간*급여*주세)) #총 공제 계산
print("*공제 후 급여 : {}원".format(int(근무시간*급여 - 근무시간*급여*원징세 - 근무시간*급여*주세))) #공제 후 급여 계산

print()

print("***** 문제2 *****")
day = int(input("경과 일을 입력하세요 : ")) #경과 일 입력받기

##오늘은 월요일

print("{}일 후는 월요일인가? {}".format(day, day % 7 == 0)) #7로 나눠서 나머지가 0이면 월요일
print("{}일 후는 화요일인가? {}".format(day, day % 7 == 1)) #7로 나눠서 나머지가 1이면 화요일
print("{}일 후는 수요일인가? {}".format(day, day % 7 == 2)) #7로 나눠서 나머지가 2이면 수요일
print("{}일 후는 목요일인가? {}".format(day, day % 7 == 3)) #7로 나눠서 나머지가 3이면 목요일
print("{}일 후는 금요일인가? {}".format(day, day % 7 == 4)) #7로 나눠서 나머지가 4이면 금요일
print("{}일 후는 토요일인가? {}".format(day, day % 7 == 5)) #7로 나눠서 나머지가 5이면 토요일
print("{}일 후는 일요일인가? {}".format(day, day % 7 == 6)) #7로 나눠서 나머지가 6이면 일요일

print()

print("***** 문제3 *****")
name = input("영문이름?(이름 성) ") #영문 이름 입력
First_name, Last_name = name.split() #입력받은 영문 이름 이름과 성 분리
ID =  Last_name[len(Last_name)-1] + First_name[1 : len(First_name)] #첫 글자를 제외한 이름과 성의 마지막 문자 합쳐서 ID 생성


birthday = input("생일?(yyyy/mm/dd) ") #생년월일 입력
year, month, day = birthday.split("/") #입력받은 생년월일 년 월 일 분리
password = "mm" + year[3] + month + day #년도의 마지막자리, 월, 일 합쳐서 패스워드 생성


print(ID) #아이디 출력
print(password) #비밀번호 출력
