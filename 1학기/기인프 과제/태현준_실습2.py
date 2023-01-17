print("20221627 태현준 실습#2")
print()

print("***** 문제1 *****")

average = (793 + 889 + 927) / 3

print(average) #평균 출력
print(round(average, 1)) # 소수점 한 자리까지 출력
print(int(average)) # 소수점 버림 해서 출력
print(round(average)) #반올림해서 출력
print()



print("***** 문제2 *****")

km = 40 * (10 **12) #km
v = 300000  #km/s
t = km / (v *60 *60 *24 * 365) #초 단위니까 연 단위로 바꿔야함

print(t, "광년") # 시간 출력
print()





print("***** 문제3 *****")
##오늘은 월요일
day1 = 15
print(str(day1) + "일 후는 화요일인가?", day1 % 7 == 1) #7로 나눠서 1이면 화요일

day2 = 143
print(str(day2) + "일 후는 화요일인가?", day2 % 7 == 1) #str()로 연결해 공백을 없애줌
