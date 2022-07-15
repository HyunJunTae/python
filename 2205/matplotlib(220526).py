import numpy as np
import matplotlib.pyplot as plt



### plot 사용.
##x = range(2011,2021)
##y = [2832, 2900, 2998, 3083, 3260, 3391, 3493, 3531, 3536, 3523]
##plt.plot(x, y) # default값으로 그림.
##plt.plot(x, y, 'g--o') # 색상, 스타일, 마커 지정
##plt.show()





### bar 사용.
##x = range(2011,2021)
##y = [2832, 2900, 2998, 3083, 3260, 3391, 3493, 3531, 3536, 3523]
##plt.bar(x, y) #막대형
##plt.title('GDP per capita') #그래프 제목을 설정
##plt.ylabel('10,000won') #y축 레이블 설정
##plt.show()


    


### plot 사용. y값 여러개 출력.
##x1 = [1965,1975,1985,1995,2005,2015]
##y1 = [130,650,2450,11600,17790,27250] #대한민국
##y2 = [890,5120,11500,42130,40560,38780] #일본
##y3 = [100,200,290,540,1760,7940] #중국
##plt.plot(x1,y1)
##plt.plot(x1,y2)
##plt.plot(x1,y3)
##plt.legend(['Korea','Japan','China']) #범례
##plt.show() 





### 매매기준율, 통화표를 numpy로 구성.
##y = np.array([1178.5,1089.39,1319.37,1468.28,
##897.3,1197.05,150.88,171.17]) # 매매기준율
##x = np.array(['USD', 'JPY', 'EUR', 'GBP',
##'CAD', 'CHF','HKD', 'CNY']) # 통화표시
##plt.plot( x, y, ‘go--’) # 그래프
##plt.show() # 화면에 표시




##numpy = np.array([
##    ["korea",1],
##    ["Japan",2],
##    ["China",3]])
##print(numpy)
### 이거 왜 되냐? 넘파이에서 같은 종류의 데이터만 담을 수 있다며
### 혹시 데이터가 리스트라서?
##
##numpy2 = np.array(["Korea",1])
##print(numpy2)
### ?? 이거도 되는디?















