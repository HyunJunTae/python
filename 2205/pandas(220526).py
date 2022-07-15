import numpy as np
import pandas as pd



# 시리즈 함수. 열 하나짜리 데이터.
data = [1,3,5,7,9]
s1 = pd.Series(data)


# index 를 이용해 인덱스 설정 가능. 인덱스는 행 개수만큼 필요함
data = [1,3,5,7,9]
s2 = pd.Series(data, index = ['영희','순희','길동','지성','Bob'])


# values, index 라는 속성을 따로 가지고있음
print(s2.values)
print(s2.index)


# 사전 객체 사용
dict1 = {"Korea":1, "Japan":2, "China":3}
s = pd.Series(dict1)


dict2 = {"Korea":[1,2,3],
         "Japan":[6,5,7],
         "China":[3,9,10]}
pp = pd.DataFrame(dict2,
                  index = ['금','은','동'])


oo = pd.DataFrame(dict1,
                  columns = ['ong'])
#이러면 오류

input2 = pd.Series( {"England":"London",
"India":"New Delhi", "USA":"Washington",
"Belgium":"Brussels"} )
df2= pd.DataFrame(input2, columns=['city'])

df3 = pd.DataFrame(s2,
                   columns = ['age'])



### 데이터프레임 함수. 행, 열이 있는 2차원 구조.
### index(행이름)과 column(열이름) 각각 있음.
##
##g_data = [ [2016, 2.8, '1.63M'],
##           [2017, 3.1, '1.73M'],
##           [2018, 3.0, '1.83M'] ]
##
##df1 = pd.DataFrame(g_data)
##print("\ndf1 : \n", df1)
##
##
###행이름 index, 열이름 column 설정
##df2 = pd.DataFrame(g_data,
##                  index = [1, 2, 3],
##                  columns = ['year', 'GDP_rate', 'GDP' ] )
##print("\ndf2 : \n", df2)





### 사전 객체 사용
##g_data = { 'year': [2016,2017,2018],
##           'GDP_rate': [2.8, 3.1, 3.0],
##           'GDP': ['1.63M','1.73M','1.83M'] }
##
##df = pd.DataFrame(g_data,
##                 index = [1, 2, 3]) # df= pd.DataFrame( data= g_data )
##print(df)
### 이렇게 하면 사전객체의 key값들이 column값들로 들어감.






### 시리즈 함수는 열 하나짜리.
### 열 하나씩 만들어서 사전객체로 만든 뒤 데이터프레임으로 나타내기.
##s1 = pd.Series([2016,2017,2018])
##s2 = pd.Series([2.8, 3.1, 3.0])
##s3 = pd.Series(['1.63M','1.73M','1.83M'])
##g_data = { 'year': s1,
##           'GDP_rate': s2,
##           'GDP': s3 }
##df = pd.DataFrame(g_data) # df= pd.DataFrame( data= g_data )
##print(df)




##s1 = pd.Series([2016,2017,2018])
##s2 = pd.Series([2.8, 3.1, 3.0])
##s3 = pd.Series(['1.63M','1.73M','1.83M'])
##g_data = { 'year': s1,
##           'GDP_rate': s2,
##           'GDP': s3 }
##df = pd.DataFrame(g_data,
##                  index = [1,2,3]) # df= pd.DataFrame( data= g_data )
##print(df)
### 위에 그냥 사전객체 바로 썼을때는 괜찮았는데
### 시리즈로 따로 만들어서 하면 왜 오류남?
##
##
##
##
##s1 = [2016,2017,2018]
##s2 = [2.8, 3.1, 3.0]
##s3 = ['1.63M','1.73M','1.83M']
##g_data = { 'year': s1,
##           'GDP_rate': s2,
##           'GDP': s3 }
##df = pd.DataFrame(g_data,
##                  index = [1,2,3]) # df= pd.DataFrame( data= g_data )
##print(df)
### 이렇게 시리즈로 안하고 그냥 리스트로 하는게 편하고 잘나옴.
##
##s1 = [2016,2017,2018]
##s2 = [2.8, 3.1, 3.0]
##s3 = ['1.63M','1.73M','1.83M']
##g_data = [s1,s2,s3]
##df = pd.DataFrame(g_data,
##                  index = [1,2,3],
##                  columns = ['year', 'GDP_rate', 'GDP']) # df= pd.DataFrame( data= g_data )
##print(df)
#### 그냥 사전개체 안쓰고 index, columns 쓰는게 알아보기도 쉽고 편함.
#### 아니지 이렇게하면 내가 원하는대로 안되잖
##
##
##
##
##s1 = [2016,2017,2018]
##s2 = [2.8, 3.1, 3.0]
##s3 = ['1.63M','1.73M','1.83M']
##df = pd.DataFrame(data = [s1, s2, s3],
##                  index = [1,2,3],
##                  columns = ['year', 'GDP_rate', 'GDP']) # df= pd.DataFrame( data= g_data )
##print(df)
### 리스트로 만들기 2.



names = ['철수', '영희', '민지', '병식']
births = ['12-25', '11-11', '05-05', '02-01']
g_data = {"Name" : names,
          "Birth" : births}
df = pd.DataFrame(g_data,
                  index = [1,2,3,4])
print(df)

gender = ['M','M','G','G']
df['성별'] = gender # 열 추가
df.loc[5] = ['한나','11-11', 'F'] # 행 추가
print(df)





























