import matplotlib.pyplot as plt
import pandas as pd

### 울릉도는 몇 월에 바람이 가장 강할까?

weather = pd.read_csv('C:/Users/user/OneDrive/바탕 화면/Python/기인프 데이터/weather.csv',
                 encoding = 'CP949')
# 한글이 들어가있어서 한글 encoding을 해줘야함.


month_data = pd.DatetimeIndex(weather['일시']).month
weather['month'] = month_data
# month_data에 '일시'열의 월 정보를 입력하고
# 원래있던 weather 데이터프레임에 month라는 이름의 새로운 열을
# month_data가지고 새로 형성.
# weather['month'] = pd.DatetimeIndex(weather['일시']).month
# 처럼 따로 변수 안쓰고 바로 할 수도 있음.


means = weather.groupby('month').mean()
# weather의 month열을 기준으로 그룹으로 나누고 평균 만들어서 means에 저장.

means1 = weather['month'].mean()
# 두 개의 차이점?
# 위에꺼는 month를 기준으로 1월부터 12월까지 나눈 후 각각 평균구하기.
# 밑에꺼는 그냥 month의 평균 구하기.



onggibot1 = weather[ weather['month'] == 1 ]
# weather 내에서 weather['month'] == 1 인 데이터만 출력.

onggibot2 = weather[ weather['month'] == 1 ]['평균 풍속(m/s)']
# weather 내에서 weather['month'] == 1 인 데이터중에서 평균풍속 열만 출력.


onggibot3 = weather[ weather['month'] == 1 ]['평균 풍속(m/s)'][0:11]
# weather 내에서 weather['month'] == 1 인 데이터중에서 평균풍속 열 앞에 10개만 출력.


onggibot4 = weather['month'] == 1
# 이렇게만 하면 True, False로 나옴.



### 언제가 풍속 제일 쎈가 그래프로 나타내기
##plt.plot(means['평균 풍속(m/s)'],
##         'blue')
##plt.show()




titanic = pd.read_csv("C:/Users/user/OneDrive/바탕 화면/Python/기인프 데이터/titanic.csv")
# 타이타닉 csv 불러오기



age = titanic [ titanic['Age'] < 20 ]
# titanic 데이터프레임에서 20세 미만인 사람만.
    

age_name = titanic [ titanic['Age'] < 20 ]["Name"]
# titanic 데이터프레임에서 20세 미만인 사람의 이름만.

age_avg = titanic['Age'].mean()
# titanic 데이터프레임에서 승객의 평균 나이

sex_survive = titanic.groupby('Sex')['Survived'].mean()
# 성별에 따른 평균 생존율
# 성별을 기준으로 그룹 나눈 후, 생존율 평균 구하기.

age_survive = titanic[ titanic['Age'] < 20 ]['Survived'].mean()
# 20세 미만 사람들의 평균 생존율.




class_survive = titanic.groupby('Pclass')['Survived'].mean()
# 클래스에 따른 평균 생존율.
# 클래스를 기준으로 그룹 나눈 후, 생존율 평균 구하기.
# 얘도 그래프 그릴 수 있네
##class_survive.plot(kind='bar')
##plt.show()

class_survive2 = titanic[['Survived','Pclass']].groupby(['Pclass']).mean()
# 클래스에 따른 평균 생존율 2.
# 타이타닉 데이터프레임에서 survived, pclass 두 줄 일단 가져오고
# 그 후 pclass로 그룹 나누고 평균 하면 자동으로 survive가 값이됨.
# 이렇게 해야 그래프를 그릴 수 있음.
# class_survive2['Survived'].plot(kind='bar')

# 위 두 개의 차이는 survived 라는 column이 있냐 없냐 차이.
# 그래도 하려면 있는게 나을듯.




class_sex_survive = titanic.groupby(['Pclass','Sex'])['Survived'].mean()
# 클래스와 성별에 따른 평균 생존율.
# 클래스와 성별을 기준으로 그룹 나눈 후, 생존율 평균 구하기

class_sex_survive2 = titanic[['Pclass','Sex','Survived']].groupby(['Pclass','Sex']).mean()





### 나이와 요금 사이에 관계가 있는지 알아보기
### 생존자 사망자 따로
##p1 = titanic[ titanic['Survived'] == 1 ]
##plt.scatter(x = p1.Age,
##            y = p1.Fare)
##plt.show()
##
##p2 = titanic[ titanic['Survived' == 0 ]]
##plt.scatter(x = p2.Age,
##            y = p2.Fare)
##plt.show()























