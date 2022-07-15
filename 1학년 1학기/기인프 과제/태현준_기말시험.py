#20221627 태현준 기말시험
import numpy as np # 넘파이 import
import matplotlib.pyplot as plt # 맷플롯립 import
import pandas as pd  # 팬더스 import


def gChk( score ) : # 성적 가져와서 매개변수 score에 저장
    if score >= 90: grade= 'A' # 90이상이면 A
    elif score >= 80: grade= 'B' # 80이상 90미만이면 B
    elif score >= 70: grade= 'C' # 70이상 80미만이면 C
    else : grade= 'D' # 그 외는 D
    return grade # A, B, C, D 학점 return해주기


print("***문제1***") # 문제1 출력
성적 = {'Hong' : 90, 'Kim':95, 'Choi':75, 'Lee':89, 'Tae' : 80} # 딕셔너리 만들기
학점 = {} # 학점 저장할 공백 딕셔너리 만들기


for i,j in 성적.items() : # 성적 딕셔너리의 키값 밸류값 각각 i, j에 가져오기
    score = gChk(j) # 밸류값인 성적 위의 함수 gChk 사용해서 학점 return받기
    학점[i] = score # 학점 딕셔너리에 키값 밸류값을 각각 이름, 학점으로 해서 넣어주기
print(학점) # 학점 딕셔너리 출력


print() # 공백 출력 줄 띄우기
print() # 공백 출력 줄 띄우기

print("***문제2***") # 문제2 출력
a = 0 # 숫자 입력받을 변수 미리 0으로 정해두기

while True : # 반복문 True인 동안 
    a = int(input("")) # 숫자 입력받기
    if a < 0 : # 받은 숫자가 음수이면 (0보다 작으면)
        break # 반복문 끝내기
    if a % 2 == 0 : # 만약 짝수이면
        print(a) # 숫자 a 출력하기. 홀수면 출력안됨.

print() # 공백 출력 줄 띄우기
print() # 공백 출력 줄 띄우기


print("***문제3***") # 문제3 출력
f = open("C:/Users/user/OneDrive/바탕 화면/Python/기인프 데이터/daily.txt",'r') # 파일 오픈.
s = f.readlines() # 파일 읽어서 s에 저장. 줄 단위로 읽어서 리스트로 반환.
# 아메리카노 라뗴 카푸치노 순

total = 0 # 판매량 저장할 변수 만들기

for i in s : # s에서 하나씩 가져오기
    i = i.split() # 공백 기준으로 split 하기
    capu = int(i[2]) # 2번열이 카푸치노. 카푸치노 판매량 capu에 저장
    total = total + capu # 판매량 계속 더해주기

print(total) # 판매량 출력
f.close() # 파일 닫기


print() # 공백 출력 줄 띄우기
print() # 공백 출력 줄 띄우기



print("***문제4***") # 문제4 출력
arr = np.array(range(1,101)) # 1부터 100까지의 정수 가지는 일차원배열 만들기. arange 사용해도 됨.
print(arr) # 배열 출력하기


print() # 공백 출력 줄 띄우기
print() # 공백 출력 줄 띄우기





print("***문제5***") # 문제5 출력

s1 = pd.Series(성적) # 성적을 이용해서 시리즈 만들기

df1 = pd.DataFrame(s1, # 만든 시리즈 이용해서 데이터프레임 만들기
                   columns = ['score']) # column은 score

df1['grade'] = list(학점.values()) # 학점 딕셔너리의 밸류값을 리스트로 만들고 이를 이용해 df1의 새로운 열을 만듦
print(df1) # df1 출력하기
print() # 공백 출력 줄 띄우기

score_mean = df1['score'].mean() # score 열의 평균을 구하고
print(score_mean) # 출력하기
print() # 공백 출력 줄 띄우기

a_grade = df1[ df1['grade']== 'A'] # A 학점인 행 구분해내서
print(a_grade) # 출력하기
print() # 공백 출력 줄 띄우기

plt.bar(list(df1.index), list(df1['score'])) # x를 df1의 인덱스인 이름으로, y를 df1의 score열로 그래프 그리기
plt.show()# 그래프 나타내기


print() # 공백 출력 줄 띄우기


print("***문제6***") # 문제6 출력

titanic = pd.read_csv("C:/Users/user/OneDrive/바탕 화면/Python/기인프 데이터/titanic.csv") # 변수 titanic에 csv 파일 읽어오기

sp_a = titanic.groupby(['Sex','Pclass'])['Age'].mean() #titanic에서 Sex, Pclass 순으로 groupby하고 그룹별로 Age평균 구하기

print(round(sp_a,1)) # Age 소수점 첫쨰자리까지 출력하기









