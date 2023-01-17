import numpy as np
import matplotlib.pyplot as plt
import pandas as pd




a = np.array([[1,2,3,4,5],
             [6,7,8,9,10],
             [11,12,13,14,15],
             [16,17,18,19,20]])

df1 = pd.DataFrame(data = a,
                   index = [1,2,3,4],
                   columns = [1,2,3,4,5])





datalist1 = np.array([[150, 170],
                      [50, 70],
                      [17,19]])

df2 = pd.DataFrame(data = datalist1,
                   index = ['키', '몸무게', '나이'],
                   columns = ['철수','영희'])



data1 = [100, 200, 300]
data2 = [400, 500, 600]
data3 = [700, 800, 900]

df3 = pd.DataFrame(data = {"ong" : data1,
                           "gi" : data2,
                           "bot" : data3},
                   index = ['옹','기','봇'])


titanic = pd.read_csv("C:/Users/user/OneDrive/바탕 화면/Python/기인프 데이터/titanic.csv")


a = titanic.groupby('Survived')['Age'].mean()
b = titanic.groupby('Pclass')['Survived'].mean()



p1 = titanic[ titanic["Survived" == 0] ]
p2 = titanic[ titanic["Survived" == 1] ]

plt.scatter(x = titanic.Survived,
            y = p1.Age)




