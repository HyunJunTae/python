import numpy as np


# 키 몸무게 리스트
h= [1.8, 1.76, 1.69, 1.86, 1.77, 1.73]
w= [75, 70, 65, 85, 77, 68]


# 키 몸무게 리스트 따로 만든 후
# 키 몸무게 넘파이 따로 만들어서 bmi 계산하기
t1 = np.array(h)
w1 = np.array(w)

bmi = w1 / (t1**2)
bmi = bmi.round(1)
a = w1[ w1 >= 75 ]



# 키 몸무게 리스트 따로 만든 후
# 이차원넘파이 하나로 키 몸무게 합쳐만들어서 bmi 계산하기
# 0번행은 키, 1번행은 몸무게
tnw1 = np.array([h,w])
bmi1= tnw1[1] / (tnw1[0]**2)
bmi1 = bmi1.round(1)



# 키 몸무게 리스트 만들 때부터 하나로 만든 후
# 이차원넘파이 하나로 키 몸무게 합쳐만들어서 bmi 계산하기
# 0번열은 키, 1번열은 몸무개
hw1 = [ [1.8, 75], [1.76, 70], [1.69, 65], [1.86, 85],
[1.77, 77], [1.73, 68] ]
tnw2 = np.array(hw1)
bmi2= tnw2[:,1] / (tnw2[:, 0]**2)
bmi2 = bmi2.round(1)
b = tnw2[ tnw2[:,1] >= 75 ] # 이건 조건 만족하는 행 통째로 출력
c = tnw2[ : , 1] >= 75 # 이건 True, False만 출력
#b = 키와몸무게[ 키와몸무게[:,0]>=1.7 ] 이거 안됨. 1.7자리에 정수만 들어갈 수 있나봄.




hw2 = [ [180, 75], [176, 70], [169, 65], [186, 85],
[177, 77], [173, 68] ]
tnw3 = np.array(hw2)
bmi3= tnw3[:,1] / (tnw3[:, 0]**2)
bmi3 = bmi3.round(1)
d = tnw3[ tnw3[:,1 ]>= 75 ] #몸무게 75 이상인 행 출력
e = tnw3[ tnw3>=75] #75보다 큰 값 출력
f = tnw3[ tnw3[:,0] >= 175 ] #키 175 이상인 행 출력.
#g = tnw3[ tnw3[ 0 , : ] >= 100 ] 값이 100 이상인 열 출력하려했는데 안되네














"""
#random.randint는 정수 난수를 생성.
players = np.zeros( (10000, 3) )
players[:, 0] = np.random.randint(155,190, size=10000)
players[:, 1] = np.random.randint(55,120, size=10000)
players[:, 2] = np.random.randint(19,30, size=10000)



# 넘파이에서 평균값 :mean  /  중앙값 : median  /  표준편차 : std
heights = players[:, 0]
print('신장 평균값:', np.mean(heights))
print('신장 중앙값:', np.median(heights))
print('신장 표준편차:', np.std(heights))

weights = players[:, 1]
print('체중 평균값:', np.mean(weights))
print('체중 중앙값:', np.median(weights))
print('체중 표준편차:', np.std(weights))

ages = players[:, 2]
print('나이 평균값:', np.mean(ages))
print('나이 중앙값:', np.median(ages))
print('나이 표준편차:', np.std(ages))
"""


"""
# 축 0으로 지정해서 세로로 계산되게 한 다음, 
평균= players.mean(axis=0)
중앙값= players.median(axis=0)
표준편차= players.std(axis=0)

# 여기서 몇 번 열 계산할지 정함.
print('신장 평균값:', 평균[0] )
print('신장 중앙값:', 중앙값[0] )
print('신장 표준편차:', 표준편차[0])

print('체중 평균값:', 평균[1])
print('체중 중앙값:', 중앙값[1] )
print('체중 표준편차:', 표준편차[1])

print('나이 평균값:', 평균[2] )
print('나이 중앙값:', 중앙값[2])
print('나이 표준편차:', 표준편차[2])
"""









"""
#random.rand는 소수점 있는 난수를 생성.
players = np.zeros( (10000, 3) )

a= 155; b=190
players[:, 0] = (b-a) * np.random.rand(10000) + a

a= 55; b=120
players[:, 1] = (b-a) * np.random.rand(10000) + a
    
a=19; b=30
players[:, 2] = np.floor((b-a) *np.random.rand(10000)) + a
"""






"""
#random.randn은 평균을 기준으로 하는 난수를 생성.
players = np.zeros( (10000, 3) )

# 표준편차는 10.
players[:, 0] = 10 * np.random.randn(10000) + 175
players[:, 1] = 10 * np.random.randn(10000) + 70
players[:, 2] = np.floor(10 * np.random.randn(10000)) + 22 #실수의 바로 아래 정수로 내림

heights = players[:, 0]
print('신장 평균값:', np.mean(heights))
print('신장 중앙값:', np.median(heights))

weights = players[:, 1]
print('체중 평균값:', np.mean(weights))
print('체중 중앙값:', np.median(weights))

ages = players[:, 2]
print('나이 평균값:', np.mean(ages))
print('나이 중앙값:', np.median(ages))
"""








































