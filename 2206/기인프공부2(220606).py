import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


##a = np.array([1,2,3,4,5])
##aa = np.array([[1,2,3,4,5],
##              [6,7,8,9,10],
##              [11,12,13,14,15]])
##aaa = np.array(range(1,21))
##aaaa = aaa.reshape(4,5)





##data = [1,3,5,7,9]
##s = pd.Series(data,
##              index = [1,2,3,4,5] )


data = [[90,90,80,70],
        [23,23,56,43],
        [12,23,34,45],
        [56,67,89,90]]
ind = ['국어','수학','영어','탐구']
col = ['철수', '희지', '소영', '동필']

df1 = pd.DataFrame(data = data,
                  index = ind,
                  columns = col)


# 리스트와 시리즈의 차이.
# 리스트는 가로로 데이터 정리되고
# 시리즈는 세로로 데이터 정리됨.




















