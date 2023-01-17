import pandas as pd
import matplotlib.pyplot as plt

data1 = [[1,2,3],
         [4,5,6],
         [7,8,9],
         [10,11,12],
         [13,14,15]]

df1 = pd.DataFrame(data = data1,
                   index = [1,2,3,4,5],
                    columns = ['ong', 'gi', 'bot'])
# df1.ong 하면 ong열 출력

# df1['ong'] 하는거랑 같음
# df1[['ong', 'gi']] 이렇게 하면 두 열 출력.
# df1.loc[1] 하면 1행 출력
# df1.loc[[1,2]] 하면 1, 2행 출력
# 괄호 써서 하는게 외우기 편할듯

print( df1[ df1['ong'] > 5 ] )
# df1에서 ong 열의 값이 5보다 큰 행만 출력






v1 = pd.read_csv('C:/Users/user/OneDrive/바탕 화면/Python/기인프 데이터/vehicle_prod.csv')
# csv 파일을 그대로 출력

v2 = pd.read_csv('C:/Users/user/OneDrive/바탕 화면/Python/기인프 데이터/vehicle_prod.csv',
                 index_col = 0)
# csv 파일의 0번 column을 index로 사용.



v2['2007'].plot(kind = "bar") # 2007 열 슬라이스해서 그래프그리기.
plt.show()


v2.loc['China'].plot(kind = "bar") # China 행 슬라이스해서 그래프그리기.
plt.show()


plt.legend(["China", "EU", "US", "Japan", "Korea", "Mexico"])
plt.plot(v2.loc["China"])
plt.plot(v2.loc["EU"])
plt.plot(v2.loc["US"])
plt.plot(v2.loc["Japan"])
plt.plot(v2.loc["Korea"])
plt.plot(v2.loc["Mexico"])
plt.show()
# 모든 나라 각각 한 행씩 따서 그래프 그리기.



##print("\nv2sum(axis = 1) : \n", v2.sum(axis=1))
### axis = 1, 즉 한 행씩 따서 합 구하기
##
##print("\nv2sum(axis = 0) : \n", v2.sum(axis=0))
### axis = 1, 즉 한 행씩 따서 합 구하기
##
##print("\nv2mean : \n", v2.mean(axis=1))
### axis = 1, 즉 한 행씩 따서 vudrbs 구하기





















