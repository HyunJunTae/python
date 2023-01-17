import numpy as np

a = np.array([1,2,3,4,5])
b = np.arange(1,21)
c = np.array(range(1,21))
d = c.reshape((4,5))

e = np.array(a%2 == 0)
f = np.array(d%2 == 0)
#True, False 값을 저장하는 것도 가능. 행, 열의 형태도 원래 넘파이랑 똑같음
ee = a[a%2 == 0]
#e는 True, False 담음. ee는 a%2를 만족하는 값 자체를 담음.


aa = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

bb = [
    [9,8,7],
    [6,5,4],
    [3,2,1]
    ]

g = np.sum(aa, axis=0)
h = np.sum(aa, axis=1)

i = np.prod(aa, axis=0)

# add(+), substract(-), multiply(*), divide(/) 는 두 개 이상의 넘파이에서 씀
# sum, prod는 하나의 넘파이를 세로(0), 가로(1)로 계산.
j = aa + bb # 그냥 리스트 더하기
k = np.array(aa) + np.array(bb)


a[1] = 10
print("a[1]=10으로 바꾸면 a = {}".format(a))

print(a[[1,2,3]])
print(a[1:4])


# d[0], d[1], d[0,0], d[1,2] 출력해보기
# d[0,0]에서 행, 열 순으로 입력. 행이 가로줄, 열이 세로. 열만 보는건 안되는듯.


dd = d[0:2 , 0:3]
ddd = d[1 , :]
dddd = d[: , 1:4]
ddddd = d[: , :]
dddddd = d
#ddddd 와 dddddd는 똑같다. =d[:,:] 하나 =d 하나 똑같다.



